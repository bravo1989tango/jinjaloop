# házi
# táblába töltsünk fel adatokat
# listán for ciklussal és annyi sort irunk ki amennyi elem van
# könnyű: lista listákat tartalmaz, mátrixot készitünk
# közepes: dictionaryt készitünk
# nehéz: classt készitünk
# cim, leirás, imdb link

from flask import Flask, render_template

app = Flask(__name__)


class filmek():
    def __init__(self, cim, leiras, IMDB):
        self.cim = cim
        self.leiras = leiras
        self.IMDB = IMDB

elso = filmek("The Shawshank Redemption",
              "Two imprisoned men bond over a number of years,"
              "finding solace and eventual redemption "
              "through acts of common decency.",
              "https://www.imdb.com/title/tt0111161/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=e31d89dd-322d-4646-8962-327b42fe94b1&pf_rd_r=ZWB8PT2QX4FAXCNQB8D8&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_1")
masodik = filmek("The Godfather",
                 "The aging patriarch of an organized crime dynasty transfers "
                 "control of his clandestine empire to his reluctant son.",
                 "https://www.imdb.com/title/tt0068646/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=e31d89dd-322d-4646-8962-327b42fe94b1&pf_rd_r=ZWB8PT2QX4FAXCNQB8D8&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_2")
harmadik = filmek("The Godfather: Part II",
                  "The early life and career of Vito Corleone in 1920s New York City is portrayed, "
                  "while his son, Michael, expands and tightens his grip on the family crime syndicate.",
                  "https://www.imdb.com/title/tt0071562/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=e31d89dd-322d-4646-8962-327b42fe94b1&pf_rd_r=ZWB8PT2QX4FAXCNQB8D8&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_3")
negyedik = filmek("The Dark Knight",
                  "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, "
                  "Batman must accept one of the greatest psychological and physical tests of his ability "
                  "to fight injustice.",
                  "https://www.imdb.com/title/tt0468569/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=e31d89dd-322d-4646-8962-327b42fe94b1&pf_rd_r=ZWB8PT2QX4FAXCNQB8D8&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_4")
otodik = filmek("12 Angry Men",
                "A jury holdout attempts to prevent a miscarriage of justice by forcing "
                "his colleagues to reconsider the evidence.",
                "https://www.imdb.com/title/tt0050083/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=e31d89dd-322d-4646-8962-327b42fe94b1&pf_rd_r=ZWB8PT2QX4FAXCNQB8D8&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_5")
hatodik = filmek("Schindler's List",
                 "In German-occupied Poland during World War II, industrialist Oskar Schindler gradually becomes concerned for "
                 "his Jewish workforce after witnessing their persecution by the Nazis.",
                 "https://www.imdb.com/title/tt0108052/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=e31d89dd-322d-4646-8962-327b42fe94b1&pf_rd_r=57QNAAWK9P8J65TW50G6&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_6")
hetedik = filmek("The Lord of the Rings: The Return of the King",
                 "Gandalf and Aragorn lead the World of Men against Sauron's army to draw his gaze "
                 "from Frodo and Sam as they approach Mount Doom with the One Ring.",
                 "https://www.imdb.com/title/tt0167260/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=e31d89dd-322d-4646-8962-327b42fe94b1&pf_rd_r=57QNAAWK9P8J65TW50G6&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_7")
nyolcadik = filmek("Pulp Fiction",
                   "The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of "
                   "diner bandits intertwine in four tales of violence and redemption.",
                   "https://www.imdb.com/title/tt0110912/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=e31d89dd-322d-4646-8962-327b42fe94b1&pf_rd_r=57QNAAWK9P8J65TW50G6&pf_rd_"
                   "s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_8")
kilencedik = filmek("Il buono, il brutto, il cattivo",
                    "A bounty hunting scam joins two men in an uneasy alliance against a third in a "
                    "race to find a fortune in gold buried in a remote cemetery.",
                    "https://www.imdb.com/title/tt0060196/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=e31d89dd-322d-4646-8962-327b42fe94b1&pf_rd_r=57QNAAWK9P8J65TW50G6&pf_rd_s="
                    "center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_9")
tizedik = filmek("The Lord of the Rings: The Fellowship of the Ring",
                 "A meek Hobbit from the Shire and eight companions set out on a journey to destroy the powerful One Ring "
                 "and save Middle-earth from the Dark Lord Sauron.",
                 "https://www.imdb.com/title/tt0120737/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=e31d89dd-322d-4646-8962-327b42fe94b1&pf_rd_r=57QNAAWK9P8J65TW50G6&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_10")

@app.route("/")
def index():
    filmek=[elso,masodik,harmadik,negyedik,otodik,hatodik,hetedik,nyolcadik,kilencedik,tizedik]
    return render_template("table.html", filmek = filmek)


if __name__ == '__main__':
    app.run()
