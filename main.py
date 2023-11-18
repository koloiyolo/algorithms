from flask import Flask, request, jsonify
import kmeans

app = Flask(__name__)


@app.route('/kmeans', methods=['POST'])
def kmeans_route():
    if request.method == 'POST':
        data = request.form['data']
        centroids = request.form['centroids']
        iters = request.form['iters']

        return jsonify('clusters', kmeans(data, centroids, iters))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
