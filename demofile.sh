
mkdir templates 
python3 scaffold.py country name
python3 scaffold.py user username country_id:references email phone password
python3 scaffold.py location lat lon name
python3 scaffold.py bowing_or_technical_school name country_id:references musical_instrument_id:references
python3 scaffold.py composer country_id:references name
python3 scaffold.py musicalinstrument name
python3 scaffold.py artist name musicalinstrument_id:references
python3 scaffold.py score composer_id:references title content time_signature key_signature location_id:references musicalinstrument_id:references artist_id:references bowing_or_technical_school_id:references
