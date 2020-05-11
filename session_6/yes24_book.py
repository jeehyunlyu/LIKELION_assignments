def extract_info(book_list):
    result = []
    for i in range(len(book_list)):
        if i % 2 == 1:
            text_info = book_list[i].find("td", {"class" : "goodsTxtInfo"})
            aupu = text_info.find("div", {"class" : "aupu"}).find_all("a")
            p_element = text_info.find_all("p")

            title = p_element[0].find("a").string
            img_src = book_list[i].find("div", {"class" : "goodsImgW"}).find("img")["src"]
            price = p_element[1].find("span", {"class" : "priceB"}).string

            if len(aupu) == 3:
                author = aupu[0]
                publisher = aupu[2]
            else:
                author = aupu[0]
                publisher = aupu[1]
        
        else:
            summary = book_list[i].find("p", {"class" : "read"}).string.strip()

        book_info = {
            "title" : title,
            "img_src" : img_src,
            "author" : author,
            "publisher" : publisher,
            "price" : price,
            "summary" : summary,
        }
        result.append(book_info)
    return result