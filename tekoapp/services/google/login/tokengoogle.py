import google.oauth2.credentials
import googleapiclient.discovery


def decode(access_token):
    credentials = google.oauth2.credentials.Credentials(
        access_token,
    )
    oauth2_client = googleapiclient.discovery.build(
        'oauth2', 'v2',
        credentials=credentials)
    return oauth2_client.userinfo().get().execute() or None