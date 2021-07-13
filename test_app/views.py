from test_app import app
import sentry_sdk

sentry_sdk.init(
    "https://b300fd52dae54b8f9919aa24f9895f8f@o919396.ingest.sentry.io/5863524",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)

class MyCustomException(Exception):
    pass

@app.route('/')
def index():
    raise MyCustomException 

@app.route('/fuckmeup')
def fuckmeup():
    raise Exception("fuckmeup")
