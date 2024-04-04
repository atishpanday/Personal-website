add_kernel = """__global__ void add_kernel(int* arr, int arr_size) {
    int id = threadIdx.x;
    if(id < arr_size) {
        arr[id] = arr[id] * arr[id];
    }
}"""

add_kernel_main_function = """int main() {
    int arr[100];
    
    for(int i = 0; i < 100; i++) {
        arr[i] = i;
    }
    
    int *dArr;
    
    cudaMalloc(&dArr, 100 * sizeof(int));
    cudaMemcpy(dArr, arr, 100 * sizeof(int), cudaMemcpyHostToDevice);
    
    add_kernel<<<1, 100>>>(dArr, 100);
    cudaDeviceSynchronize();
    
    cudaMemcpy(arr, dArr, 100 * sizeof(int), cudaMemcpyDeviceToHost);
    
    return 0;
}"""

kuramoto_kernel = """#define lambda 0.05
#define N 100

__global__ void kuramoto(int *A, double *theta, double *w, double *k, double *prevk, int iter, double adder) {
	int id = threadIdx.x;
	
	// first set it equal to the initial omega values
	k[id] = w[id];
	
	for(int i = 0; i < N; i++) {
		k[id] += lambda * A[i * N + id] * sin(theta[iter * N + i] - (theta[iter * N + id] + (adder * prevk[id])));
	}
}"""
