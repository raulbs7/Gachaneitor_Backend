from argparse import ArgumentParser
from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker, InputStream
from web.antlr.GachaneitorLexer import GachaneitorLexer
from web.antlr.GachaneitorParser import GachaneitorParser
from web.antlr.GachaneitorErrorListener import GachaneitorErrorListener
from web.antlr.CustomGachaneitorListener import CustomGachaneitorListener

def web_main(text):
    input_stream = InputStream(text)
    lexer = GachaneitorLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = GachaneitorParser(stream)

    parser.removeErrorListeners()
    parser.addErrorListener(GachaneitorErrorListener())
    tree = parser.inicio()

    listener = CustomGachaneitorListener()
    walker = ParseTreeWalker()

    walker.walk(listener, tree)
    recetas = listener.recetas
    return recetas

def main(args):
    input_stream = FileStream(args.input_file, encoding="utf-8")
    lexer = GachaneitorLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = GachaneitorParser(stream)

    parser.removeErrorListeners()
    parser.addErrorListener(GachaneitorErrorListner())
    tree = parser.inicio()
    
    listener = CustomGachaneitorListener()
    walker = ParseTreeWalker()

    try:
        walker.walk(listener, tree)
    except Exception as e:
        print(e)

    recetas = listener.recetas
    return recetas

def build_argparser():
    argparser = ArgumentParser()
    argparser.add_argument(
        "-i", "--input_file",
        help="Cadena de entrada del procesador de lenguajes."
    )
    argparser.add_argument(
        "-o", "--output_dir",
        help="Directorio donde el lenguaje de salida será guardado.",
        default="."
    )
    return argparser

 
if __name__ == '__main__':
    parser = build_argparser()
    main(parser.parse_args())