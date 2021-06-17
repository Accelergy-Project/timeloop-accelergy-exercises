# baseline
timeloop-model ../arch/1level.arch.yaml ../map/dot-product-1level.yaml \
../prob/dot-product.prob.yaml -o ../output/no-optimization

# apply gating optimization
timeloop-model ../arch/1level.arch.yaml ../map/dot-product-1level.yaml \
../sparse-opt/*.yaml ../prob/dot-product.prob.yaml -o ../output/gating
