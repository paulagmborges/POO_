Programação Orientada a Objetos:<br>

É um estilo de programção que se concentra em organizar o código em unidades chamadas "objetos".<br>
Pegamos objetos do mundo real e modelamos em classe.<br>
Por exemplo para modelar um animal, começamos com o class e usamos o def __init__ para inicializar (construtor) e colocamos o que queremos para modelar.<br><br>

_ = privado (atributos não devem ser acessados fora da classe).<br>
<br><br>
__= totalmete privado(atributos podem ser alterados para não dar conflito com a classe).<br>
<br><br>
  = público<br>
<br><br>
  Self - permite que os métodos acessem e modifiquem os atributos da instancia.<br>
<br><br>
-Herança simples- herda da classe.No exercício de Animal.<br>
<br><br>
-Herança múltipla - herda caracteristicas de duas classes diferentes, no exercício herda do Animal e Gato.<br>
<br><br>
-Classe abstrata - São aquelas classes que não podem ser instanciadas diretamenete.<br>
Geralmente definem métodos (comportamentos) que devem ser implementados por subclasses.<br>

from abc import ABC, abstractclassmethod -> importar para implmentar a classe abstrata.<br>
Classe base para criar classes abstratas em pyhton, o abstractclassmethod é um decorador de python que é utilizado para definir métodos abstratos. Decorador é um função que vai permitir que outras classes modifiquem ela.<br>