C_DICT = {
    "せやな":"c_seyana",
    "アンイク":"c_an19",
    "ｱﾝｲｸ":"c_an19",
    "ダメです":"c_bad",
    "泣いてます":"c_cry",
    "おつかれ":"c_gj",
    "おつかれ!":"c_gj",
    "おつかれ！":"c_gj",
    "おつ":"c_gj",
    "おはよう":"c_gm",
    "おやすみ":"c_gn",
    "いいね":"c_good",
    "よろしくね":"c_greet",
    "は？":"c_ha",
    "は?":"c_ha",
    "こんにちは":"c_hello",
    "いくぜ":"c_ikuze",
    "いくぜ！":"c_ikuze",
    "いくぜ!":"c_ikuze",
    "遊び行かん？":"c_invite",
    "遊び行かん?":"c_invite",
    "ねぇ！":"c_nee",
    "ねえ！":"c_nee",
    "ねぇ!":"c_nee",
    "ねえ!":"c_nee",
    "きみかわいいね":"c_nkgw",
    "nkgw":"c_nkgw",
    "おう":"c_oh",
    "OK":"c_ok",
    "ok":"c_ok",
    "おｋ":"c_ok",
    "おk":"c_ok",
    "おもんな":"c_omonna",
    "ぴえん":"c_pien",
    "うるさい":"c_quiet",
    "静かに":"c_quiet",
    "シー":"c_quiet",
    "^^":"c_smile",
    "すまん":"c_sry",
    "sry":"c_sry",
    "ありがとう":"c_ty",
    "ありがとうございます":"c_ty",
    "なんだぁ？てめぇ":"c_wtf",
    "なんだぁ?てめぇ":"c_wtf",
    "ｱﾘｶﾞﾄｳｺﾞｻﾞｲﾏｽ!":"takeshi",
    "確定":"kakutei",
    "審議":"shingi",
}

def get_word_list():
    word_list = "```"
    for word in C_DICT.keys():
        word_list += word + "\n"
    
    word_list += "```"
    return word_list

def get_imgID_list():
    id_list = "```"
    img_IDs = sorted(set(C_DICT.values()))
    for id in img_IDs:
        id_list += id + "\n"

    id_list += "```"
    return id_list

if __name__ == "__main__":
    pass