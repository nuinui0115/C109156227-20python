a=set("春眠不覺曉，處處聞啼鳥。 夜來風雨聲， 花落知多少。")
b=set("紅豆生南國，春來發幾枝?願君多采擷，此物最相思。")
a.remove("，")
a.remove("。")
b.remove("，")
b.remove("。")
b.remove("?")
print(a&b)







