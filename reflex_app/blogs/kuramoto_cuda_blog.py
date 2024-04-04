import reflex as rx
from .blog_layout import blog_layout
from .kuramoto_cuda_codes import add_kernel, add_kernel_main_function, kuramoto_kernel


@rx.page(route="/kuramoto-cuda-blog")
def kuramoto_cuda_blog():
    return blog_layout(
        rx.vstack(
            rx.heading(
                "CUDA: Solving Kuramoto oscillators using GPU parallelization",
                size="9",
                color_scheme="indigo",
            ),
            rx.heading("What is CUDA?", size="7", color_scheme="indigo"),
            rx.text(
                "If you have a gaming PC, it contains either an NVIDIA or an AMD GPU."
            ),
            rx.text(
                "In either case, what your PC carries is an immense amount of computational power, power that you can utilize in many ways to write highly parallel code that runs much faster than the most optimal code you can write on the CPU."
            ),
            rx.text(
                "There are ways to take advantage of the compute capabilities of your GPU. Frameworks like OpenCL provide you with functions and APIs to interact with your GPU; command it to perform certain tasks for you."
            ),
            rx.text(
                "CUDA is another platform that you can use to specifically utilize NVIDIA GPUs for your computations. CUDA stands for Compute Unified Device Architecture. It is a parallel computing platform and a programming model developed by NVIDIA for general computing on GPUs."
            ),
            rx.text(
                "Your CPU may have 6 cores, 8 cores or maybe even 16 cores. Even if you utilized every core in your CPU, you'd hardly get any amount of parallelization done."
            ),
            rx.text(
                "Your GPU, on the other hand, has hundreds of thousands of cores. Each core is capable of performing computations, reliably and quickly. This can be taken advantage of by using platforms like CUDA on NVIDIA GPUs."
            ),
            rx.heading("How is it better?", size="7", color_scheme="indigo"),
            rx.text(
                "Suppose you have N electrons under a time-varying electric field. Suppose you want to calculate the positions or the speeds of each electron due to the influence of a time-varying electric field at different points in time."
            ),
            rx.text(
                "Normally, you'd run a loop from i = 0 to N - 1, and then for each iteration, you'd calculate the position/speed of the electron, keeping in mind the value of the electric field at that moment."
            ),
            rx.text(
                "This loop could take a huge amount of time to run, depending on the size of N, and the period of time. This is the problem with sequential programming."
            ),
            rx.text(
                "But, with parallel programming, you could delegate the task of calculating the position/speed of each electron to a different GPU core. Now, each core would perform the computation simultaneously. This means, even if N grows larger, your program would still require the same amount of time to run. It also means, our parallel program would run N times faster than the sequential program."
            ),
            rx.heading("What does CUDA look like?", size="7", color_scheme="indigo"),
            rx.text(
                "Let's write a simple program that squares the elements of an array."
            ),
            rx.box(
                rx.code_block(
                    add_kernel,
                    language="cpp",
                    can_copy=True,
                    show_line_numbers=True,
                ),
                width="100%",
            ),
            rx.text(
                "Notice there is no for loop in the above code. The kernel simply uses an id to access the id'th value of the array and calculates its new value. This is possible because the kernel is actually being run by multiple threads at the same time. Each thread has a unique id as soon as the kernel is launched. This id can be accessed using threadIdx.x."
            ),
            rx.text(
                "Thus, if the arr_size is 100, we can launch the kernel with 100 threads, each thread having a unique threadIdx.x value from 0 to 99. Each of these threads then accesses the array at 0th to 99th index, computing the values as needed."
            ),
            rx.heading("Calling the kernel", size="7", color_scheme="indigo"),
            rx.text(
                "The kernel can be called from the main function in the following manner."
            ),
            rx.box(
                rx.code_block(
                    add_kernel_main_function,
                    language="cpp",
                    can_copy=True,
                    show_line_numbers=True,
                ),
                width="100%",
            ),
            rx.text(
                "A lot of things happened here. If you are brand new to CUDA, you should stick around."
            ),
            rx.text(
                "First, we declared an empty array called arr of size 100. We then initialized this array to the values 0, 1, 2, ..., 99. Then, we declared another array dArr. This array will be accessible to the GPU, because the memory allocated to this array was done using cudaMalloc(), which allocates memory on the GPU. Then, we used cudaMemcpy() to copy the contents of arr to dArr.The cudaMemcpyHostToDevice enum tells the compiler that the copy of contents of memories must be done from the Host (CPU) to the device (GPU). It is also possible to do it the other way round, as we do in the second cudaMemcpy()."
            ),
            rx.text(
                "Then comes the kernel call. Here, you might notice that the kernel call looks slightly different from usual function calls. The addition of <<<1, 100>>> indicates the number of threads and blocks that must be used while launching the kernel. This means, that whenever we call a kernel, we must decide how many cores will be used to run the kernel. In this case, we used 1 block containing 100 threads to launch our add_kernel kernel. This suffices our requirements for this basic example as we only need 100 threads to access the 100 elements in our array. We then pass in the device array (dArr) and the size of the array as 100."
            ),
            rx.heading("Kuramoto Oscillators", size="7", color_scheme="indigo"),
            rx.text(
                "A system of differential equations, used to model the synchronous behavior of coupled oscillators. In laymen's terms, these are a set of equations that explain how every oscillator in a network of coupled oscillators starts to synchronize with each other."
            ),
            rx.text(
                "Every oscillator has its own natural frequency of oscillation. When two oscillators are coupled together, they start to oscillate with the same frequency after a period of time. This phenomena is called synchronization. Kuramoto oscillators tell us mathematically whether a network of oscillators connected in some fashion will synchronize or not, given a certain coupling strength."
            ),
            rx.heading(
                "Solving the Kuramoto equations using CUDA",
                size="7",
                color_scheme="indigo",
            ),
            rx.text(
                "I wrote a simple kernel that solves the individual Kuramoto equation for each node simultaneously. The kernel looks like this:"
            ),
            rx.box(
                rx.code_block(
                    kuramoto_kernel,
                    language="cpp",
                    can_copy=True,
                    show_line_numbers=True,
                ),
                width="100%",
            ),
            rx.text(
                "Since the computation of every node occurs simultaneously, the speed of execution of the program increases N-fold."
            ),
            rx.text(
                "Check out the full code on my github: https://www.github.com/atishpanday/Kuramoto-Oscillators"
            ),
            width="60%",
            spacing="7",
            margin="40px",
        ),
    )
