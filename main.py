import PIL.Image

# caracteres ascii que irão construir a saída de texto
# Um pixel mais escuro será traduzido em "@" e um mais claro em "."
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]


# Redimensionando a imagem de acordo com a nova altura
class FormatImage:
    def resize_image(self, image, nova_largura=50):
        largura, altura = image.size  # Pega a largura e a altura da imagem
        razao = altura / largura  # proporção entre altura e largura
        nova_altura = int(nova_largura * razao)
        # image.resize() retorna um objeto Image
        nova_imagem = image.resize((nova_largura, nova_altura))
        return nova_imagem

    # Convertendo cada pixel para escalas de cinza
    def tornar_cinza(self, image):
        escala_cinza = image.convert("L")
        return escala_cinza

    # Convertendo pixels para String
    def pixel_para_ascii(self, image, contrast=25):
        # Retorna o conteúdo desta imagem como um objeto de sequência contendo valores de pixel.
        pixels = image.getdata()
        caracteres = " ".join([ASCII_CHARS[pixel // contrast]
                              for pixel in pixels])
        return caracteres


class MakeImage(FormatImage):
    def main(self, nova_largura=100):
        # Abrir a imagem atraves da entrada do usuario
        keep = 'sim'
        while keep == 'sim':
            path = input("Digite o caminho da imagem:\n")
            try:
                image = PIL.Image.open(path)
            except:
                print(path, "Esse não é o caminho correto.")

            # Convertendo imagem para ASCII
            image_name = input("Digite o nome para o seu arquivo: \n")
            print("Escolha um número para Padrão de Contraste:")
            contrast = int(input("25 - alto, 30 - médio, 40 - baixo: \n"))
            n = int(
                input("Quantas vezes gostaria de repetir a imagem no arquivo: \n"))
            new_image_data = self.pixel_para_ascii(
                self.tornar_cinza(self.resize_image(image)), contrast=contrast)

            # Formatando
            pixel_count = len(new_image_data)
            ascii_image = "\n".join(new_image_data[i:(i + nova_largura)]
                                    for i in range(0, pixel_count, nova_largura))  # Vai juntar todos os caracteres

            # Printar o resultado mediante quantidade de repetições desejadas
            for k in range(n):
                print(ascii_image)
                k+1
            # Salvando o Resultado no "ascii_image.json"
            with open(f"{image_name}.json", "w") as f:
                for k2 in range(n):
                    f.write(ascii_image)
                    f.write("\n\n")
                    k2+1

            keep = input(
                'Deseja converter mais uma imagem ? Digite sim ou não: \n')


MakeImage().main()
