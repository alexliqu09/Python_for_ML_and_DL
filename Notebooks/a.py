class Laptop:
    def __init__(
        self, name="Asus", processor="Intel", gpu="GEFORCE_RTX_3070", ram="8GB"
    ):
        self.name = name
        self.processor = processor
        self.gpu = gpu
        self.ram = ram

    def __str__(self):
        return f"The laptop {self.name}, the processor is {self.processor}, the GPU: {self.gpu} and the ram is {self.ram}."

    def __del__(self):
        print(f"Delete the objetc:  {self.__str__()}")
