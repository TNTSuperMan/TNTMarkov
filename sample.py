import MeCab
import tntmarkov as mkv

def main():
    print("TNTMarkov サンプルプログラム")
    print("~ Broken Law Generator ~\n")
    with open("model.txt", "r", encoding="utf-8") as f:
        text = f.read()
    mecab = MeCab.Tagger("-Owakati")
    words = mecab.parse(text)
    model = mkv.MakeModel(words.split(" "))
    while(input() == ""):
        print(mkv.MekeMarkovText(model, "第", "。"))


if(__name__ == "__main__"):
    main()