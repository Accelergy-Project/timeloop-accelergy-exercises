from typing import Optional
import os
import threading
import timeloopfe.v4 as tl

Specification = tl.Specification
THIS_SCRIPT_DIR = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
EXAMPLE_DIR = os.path.join(THIS_SCRIPT_DIR, "example_designs")


def get_architecture_targets():
    targets = []
    for root, dirs, files in os.walk(EXAMPLE_DIR):
        if "arch.yaml" in files:
            c = open(os.path.join(root, "arch.yaml")).read()
            if "version: 0.4" not in c:
                continue
            targets.append(os.path.relpath(root, EXAMPLE_DIR))
    return sorted(targets)


def run_mapper(
    arch_target,
    problem: Optional[str] = None,
    generate_ref_outputs: Optional[bool] = False,
    remove_sparse_opts: Optional[bool] = False,
):
    odir = "ref_outputs" if generate_ref_outputs else "outputs"
    output_dir = f"{EXAMPLE_DIR}/{arch_target}/{odir}"

    if problem:
        output_dir = f"{output_dir}/{os.path.basename(problem).split('.')[0]}"
    else:
        output_dir = f"{output_dir}/default_problem"

    jinja_parse_data = {"architecture": arch_target}
    if problem:
        jinja_parse_data["problem"] = problem

    print(f"\n\nRunning mapper for target {arch_target} in {output_dir}...")

    if os.path.exists(output_dir):
        os.system(f"rm -rf {output_dir}")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    spec = tl.Specification.from_yaml_files(
        os.path.join(EXAMPLE_DIR, "top.yaml.jinja2"),
        jinja_parse_data=jinja_parse_data,
    )
    if remove_sparse_opts:
        for s in spec.get_nodes_of_type(
            (
                tl.sparse_optimizations.ActionOptimizationList,
                tl.sparse_optimizations.RepresentationFormat,
                tl.sparse_optimizations.ComputeOptimization,
            )
        ):
            s.clear()

    tl.call_mapper(
        spec,
        output_dir=output_dir,
        dump_intermediate_to=output_dir,
    )
    assert os.path.exists(f"{output_dir}/timeloop-mapper.stats.txt"), (
        f"Mapper did not generate expected output for {arch_target}. "
        f"Please check the logs for more details."
    )


if __name__ == "__main__":
    import argparse

    arch_targets = get_architecture_targets()

    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        "--clear-outputs",
        default=False,
        action="store_true",
        help="Clear all generated outputs",
    )
    argparser.add_argument(
        "--architecture",
        type=str,
        default="eyeriss_like",
        help="Architecture to run in the example_designs directory. "
        "If 'all' is given, all architectures will be run.",
    )
    argparser.add_argument(
        "--generate-ref-outputs",
        default=False,
        action="store_true",
        help="Generate reference outputs instead of outputs",
    )
    argparser.add_argument(
        "--problem",
        type=str,
        default=None,
        help="Problem to run in the layer_shapes directory. If a directory is "
        "specified, all problems in the directory will be run. If not specified, "
        "the default problem will be run.",
    )
    argparser.add_argument(
        "--n_jobs", type=int, default=16, help="Number of jobs to run in parallel"
    )
    argparser.add_argument(
        "--remove-sparse-opts",
        default=False,
        action="store_true",
        help="Remove sparse optimizations",
    )

    args = argparser.parse_args()
    if args.clear_outputs:
        os.system(f"rm -rf {EXAMPLE_DIR}/*/outputs")
        os.system(f"rm -rf {EXAMPLE_DIR}/*/ref_outputs")
        os.system(f"rm -rf {EXAMPLE_DIR}/*/*/outputs")
        os.system(f"rm -rf {EXAMPLE_DIR}/*/*/ref_outputs")
        exit(0)

    arch = args.architecture
    if str(arch).lower() == "all":
        arch = arch_targets
    arch = [arch] if isinstance(arch, str) else arch
    arch = arch_targets[0] if not arch else arch

    problems = [None]
    if args.problem:
        problem = os.path.join(THIS_SCRIPT_DIR, "layer_shapes", args.problem)
        if os.path.isdir(problem):
            problems = [os.path.join(problem, f) for f in os.listdir(problem)]
        else:
            problems = [problem]

    import joblib

    joblib.Parallel(n_jobs=args.n_jobs)(
        joblib.delayed(run_mapper)(
            a, p, args.generate_ref_outputs, args.remove_sparse_opts
        )
        for a in arch
        for p in problems
    )
