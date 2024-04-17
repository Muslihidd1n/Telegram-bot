# Flask









dastur = Flask("Mashq")


@dastur.route('/salom/<ism>')

def salomlash(ism):
    return f"<h1>Salom, {ism}!</h1>"

dastur.run()

# @dastur.route('/books')
# def books():
#     with connect('kitoblar.db') as db:
#         kursor = db.cursor()
#         kursor.execute(
#             """
#             select * from Kitob
#             """
#         )
#         hammasi = kursor.fetchall()
#     return render_template('book_records.html',kitoblar = hammasi)
#
# @dastur.route('/Ronaldoning oltin toplari')
# def tanishtish():
#     return ("<h1>Roanldo</h1>"\
#             "<h4>Ronaldo 5 marotaba halollik bilan oltin topni qolga kiritgan</h1>"\
#             "<a href='/'><h1>/sahifa</h1></a>")
#
#
# @dastur.route('/sahifa/IELTS.IDP')
# def guide():
#     return ("<h1>IELTS IDP ga hush kelibsiz!<h1>"
#             "<h4>IELTS IDP 2016 yili O'zbekistonga kirib keldi<h4>"
#             "<h4>IELTS IDP ni Umidjon Ishmuhammedov olib kirdi<h4>")
#
#
# @dastur.route('/vaqt')
# def vaqt():
#     return redirect("/sahifa")





# "Home work 3"
#
# "1 masala"
#
#
# "2 masala"
#
# @dastur.route('/salom/<ism>')
#
# def salomlash(ism):
#     return f"<h1>Salom, {ism}!</h1>"

# dastur.run()