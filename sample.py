import MeCab
import tntmarkov as mkv

def main():
    with open("model.txt", "r", encoding="utf-8") as f:
        text = f.read()
    mecab = MeCab.Tagger("-Owakati")
    words = mecab.parse(text)
    model = mkv.MakeModel(words.split(" "))
    while(input() == ""):
        print(mkv.MekeMarkovText(model, first="吾輩", end="。"))


if(__name__ == "__main__"):
    main()