import pyperclip

# Core
from core.comandos import *
from core.database import *

# Features
from features.screenshots import *
from features.albuns_fotos import *

# Services
from services.tmdb import *
from services.imgur import *
from services.spotify import *
from services.youtube import *
from services.wikipedia import *
from services.google_drive import *

# Utils
from utils.files import *
from utils.random import *
from utils.requests import *

class LuanaCore:

    def iniciar():
        cmd = Comandos.ouvir()

        if cmd == 'luana':
            file_path = 'storage/screenshots/'
            file_name = Random.string(36)
            file_ext = '.png'

            Screenshots(
                file_path = file_path,
                file_name = file_name,
                file_extension = file_ext
            ).capturar_tela(
                Comandos.falar('Captura de tela salva com sucesso')
            )

            pyperclip.copy(
                Imgur(
                    '019ba84af47bc6b'
                ).enviar_imagem(
                    image_path = file_path + file_name + file_ext
                )
            )

            Comandos.falar('Link copiado com sucesso.')