from flask import Flask

app = Flask(__name__)

class Weblab:
    # name of the weblab = [totalRequestsServed, [WeblabName, Traffic %, requestsServered]]
    PRODUCTS_WITHCURRENCY = [0, ['Feature1', 5, 0]]
    
    def getTreatment(self, weblab_name):
        print("weblab_name : " + weblab_name)
        match weblab_name:
            case 'PRODUCTS_WITHCURRENCY':
                print("weblab_name : " + weblab_name)
                #for simplicity first N requests in every 100 request will be served to weblabs
                # N is equal to Traffic % mentioned
                if Weblab.PRODUCTS_WITHCURRENCY[0]%100 < Weblab.PRODUCTS_WITHCURRENCY[1][1]:
                    Weblab.PRODUCTS_WITHCURRENCY[0] += 1
                    Weblab.PRODUCTS_WITHCURRENCY[1][2] += 1
                    print(Weblab.PRODUCTS_WITHCURRENCY[1][0])
                    return Weblab.PRODUCTS_WITHCURRENCY[1][0]
                else:
                    return 'Regular'
            case _:
                print("No Weblab requested")
                return 'No Weblab requested'


@app.route('/getProducts')
def index():
    print("entered")
    weblab = Weblab()
    print(Weblab.PRODUCTS_WITHCURRENCY)
    if ('Feature1' == weblab.getTreatment('PRODUCTS_WITHCURRENCY')):
        return withCurrency()
    else:
        return withoutCurrency()

def withoutCurrency():
    return "id, name, price"

def withCurrency():
    return "id, name, price, currency"

if __name__ == "__main__":
    app.run(debug=True)
