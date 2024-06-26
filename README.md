Run the Python script `python webhook.py` to start the Flask app.
Expose the Flask app with ngrok by running `ngrok http 5000` and replace the ngrok URL in the `main.yml` file in `action-repo`.
After running, perform actions like push, pull request, and merge. You can see the actions on the Flask app server at http://localhost:5000/.
After making the actions, they will be visible on the server and stored in MongoDB.
