from flask import Flask, render_template, request, session
import os
from yourappdb import query_db, get_db
from flask import g

app = Flask(__name__)
app.secret_key="any string"
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
init_db()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def hello_world():
    user = query_db('select * from contacts')
    the_username = "anonyme"
    one_user = query_db('select * from contacts where first_name = ?',
                [the_username], one=True)
    return render_template("hey.html", users=user, one_user=one_user, the_title="my title")
@app.route("/add_one_country", methods=["GET","POST"])
def add_one_country():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into country (name) values (:name)",hey)
        user = query_db('select * from country')

        return render_template("countryform.html", countrys=user, one_user=one_user, the_title="add new country")


    user = query_db('select * from country')
    one_user = query_db("select * from country limit 1", one=True)
    return render_template("countryform.html", countrys=user, one_user=one_user, the_title="add new country")

@app.route("/add_one_user", methods=["GET","POST"])
def add_one_user():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslescountry= query_db("select * from country")

        one_user = query_db("insert into user (username,country_id,email,phone,password) values (:username,:country_id,:email,:phone,:password)",hey)
        user = query_db('select * from user')

        last_user = query_db("select * from user where email = ? and password = ?",[hey["email"], hey["password"]], one=True)
        session["current_user_id"]=last_user["id"]
        for x in ['username','country_id','email','phone','password']:
            session[x]=hey[x]


        return render_template("userform.html", users=user, one_user=one_user, the_title="add new user", touslescountry=touslescountry)


    touslescountry= query_db("select * from country")

    user = query_db('select * from user')
    one_user = query_db("select * from user limit 1", one=True)
    return render_template("userform.html", users=user, one_user=one_user, the_title="add new user", touslescountry=touslescountry)


@app.route("/user_sign_out", methods=["GET","POST"])
def user_sign_out():
    if request.method == 'POST':
        session["current_user_id"]=""
        for x in ['username','country_id','email','phone','password']:
            session[x]=""
        return redirect("/")


@app.route("/user_log_in", methods=["GET","POST"])
def user_login():
    if request.method == 'POST':
        hey=request.form
        last_user = query_db("select * from user where email = ? and password = ?",[hey["email"], hey["password"]], one=True)
        try:
            session["current_user_id"]=last_user["id"]
            for x in ['username','country_id','email','phone','password']:
                session[x]=hey[x]
        except:
            return render_template("userlogin.html")
    return render_template("userlogin.html")
@app.route("/add_one_location", methods=["GET","POST"])
def add_one_location():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into location (lat,lon,name) values (:lat,:lon,:name)",hey)
        user = query_db('select * from location')

        return render_template("locationform.html", locations=user, one_user=one_user, the_title="add new location")


    user = query_db('select * from location')
    one_user = query_db("select * from location limit 1", one=True)
    return render_template("locationform.html", locations=user, one_user=one_user, the_title="add new location")

@app.route("/add_one_bowing_or_technical_school", methods=["GET","POST"])
def add_one_bowing_or_technical_school():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslescountry= query_db("select * from country")

        touslesmusical_instrument= query_db("select * from musical_instrument")

        one_user = query_db("insert into bowing_or_technical_school (name,country_id,musical_instrument_id) values (:name,:country_id,:musical_instrument_id)",hey)
        user = query_db('select * from bowing_or_technical_school')

        return render_template("bowing_or_technical_schoolform.html", bowing_or_technical_schools=user, one_user=one_user, the_title="add new bowing_or_technical_school", touslescountry=touslescountry, touslesmusical_instrument=touslesmusical_instrument)


    touslescountry= query_db("select * from country")

    touslesmusical_instrument= query_db("select * from musical_instrument")

    user = query_db('select * from bowing_or_technical_school')
    one_user = query_db("select * from bowing_or_technical_school limit 1", one=True)
    return render_template("bowing_or_technical_schoolform.html", bowing_or_technical_schools=user, one_user=one_user, the_title="add new bowing_or_technical_school", touslescountry=touslescountry, touslesmusical_instrument=touslesmusical_instrument)

@app.route("/add_one_composer", methods=["GET","POST"])
def add_one_composer():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslescountry= query_db("select * from country")

        one_user = query_db("insert into composer (country_id,name) values (:country_id,:name)",hey)
        user = query_db('select * from composer')

        return render_template("composerform.html", composers=user, one_user=one_user, the_title="add new composer", touslescountry=touslescountry)


    touslescountry= query_db("select * from country")

    user = query_db('select * from composer')
    one_user = query_db("select * from composer limit 1", one=True)
    return render_template("composerform.html", composers=user, one_user=one_user, the_title="add new composer", touslescountry=touslescountry)

@app.route("/add_one_musicalinstrument", methods=["GET","POST"])
def add_one_musicalinstrument():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into musicalinstrument (name) values (:name)",hey)
        user = query_db('select * from musicalinstrument')

        return render_template("musicalinstrumentform.html", musicalinstruments=user, one_user=one_user, the_title="add new musicalinstrument")


    user = query_db('select * from musicalinstrument')
    one_user = query_db("select * from musicalinstrument limit 1", one=True)
    return render_template("musicalinstrumentform.html", musicalinstruments=user, one_user=one_user, the_title="add new musicalinstrument")

@app.route("/add_one_artist", methods=["GET","POST"])
def add_one_artist():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesmusicalinstrument= query_db("select * from musicalinstrument")

        one_user = query_db("insert into artist (name,musicalinstrument_id) values (:name,:musicalinstrument_id)",hey)
        user = query_db('select * from artist')

        return render_template("artistform.html", artists=user, one_user=one_user, the_title="add new artist", touslesmusicalinstrument=touslesmusicalinstrument)


    touslesmusicalinstrument= query_db("select * from musicalinstrument")

    user = query_db('select * from artist')
    one_user = query_db("select * from artist limit 1", one=True)
    return render_template("artistform.html", artists=user, one_user=one_user, the_title="add new artist", touslesmusicalinstrument=touslesmusicalinstrument)

@app.route("/add_one_score", methods=["GET","POST"])
def add_one_score():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslescomposer= query_db("select * from composer")

        tousleslocation= query_db("select * from location")

        touslesmusicalinstrument= query_db("select * from musicalinstrument")

        touslesartist= query_db("select * from artist")

        touslesbowing_or_technical_school= query_db("select * from bowing_or_technical_school")

        one_user = query_db("insert into score (composer_id,title,content,time_signature,key_signature,location_id,musicalinstrument_id,artist_id,bowing_or_technical_school_id) values (:composer_id,:title,:content,:time_signature,:key_signature,:location_id,:musicalinstrument_id,:artist_id,:bowing_or_technical_school_id)",hey)
        user = query_db('select * from score')

        return render_template("scoreform.html", scores=user, one_user=one_user, the_title="add new score", touslescomposer=touslescomposer, tousleslocation=tousleslocation, touslesmusicalinstrument=touslesmusicalinstrument, touslesartist=touslesartist, touslesbowing_or_technical_school=touslesbowing_or_technical_school)


    touslescomposer= query_db("select * from composer")

    tousleslocation= query_db("select * from location")

    touslesmusicalinstrument= query_db("select * from musicalinstrument")

    touslesartist= query_db("select * from artist")

    touslesbowing_or_technical_school= query_db("select * from bowing_or_technical_school")

    user = query_db('select * from score')
    one_user = query_db("select * from score limit 1", one=True)
    return render_template("scoreform.html", scores=user, one_user=one_user, the_title="add new score", touslescomposer=touslescomposer, tousleslocation=tousleslocation, touslesmusicalinstrument=touslesmusicalinstrument, touslesartist=touslesartist, touslesbowing_or_technical_school=touslesbowing_or_technical_school)

