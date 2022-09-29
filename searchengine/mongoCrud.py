import pymongo


class MongoDB:
    def __init__(self):
        self.myClient = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.myClient["spiderweb"]

    def get_contents(self, collection, search_word):
        data = self.db[collection]
        results = []
        for item in data.find({"$text": {"$search": search_word}}):
            item.pop('_id')
            results.append(item)
            print(item)
        return results

    def get_keywords(self, collection, search_word):
        data = self.db[collection]
        results = []
        for item in data.find({"$text": {"$search": search_word}}):
            item.pop('_id')
            results.append(item)
        return results

    def get_pdfs(self, collection, search_word):
        pdf_data = self.db[collection]
        pdf_results = []
        for item in pdf_data.find({"$text": {"$search": search_word}}):
            item.pop('_id')
            pdf_results.append(item)
        return pdf_results

    def get_image(self, collection, search_word):
        data = self.db[collection]
        results = []
        for item in data.find({"$text": {"$search": search_word}}):
            item.pop('_id')
            results.append(item)
        return results


# obj = MongoDB()
# print(obj.get_contents('contents', 'd'))






