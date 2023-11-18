from flask import Flask, request, jsonify
import kmeans

app = Flask(__name__)


@app.route('/kmeans', methods=['POST'])
def kmeans_route():
    if request.method == 'POST':
        data = request.form['data']
        centroids = request.form['centroids']
        iters = request.form['iters']

        return jsonify('clusters', kmeans.kmeans(data, centroids, iters))


if __name__ == '__main__':
    app.run(debug=True)

