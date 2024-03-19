import re

import requests

DEFAULT_HEADERS ={
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
}

resp = requests.get("https://twitter.com/", headers=DEFAULT_HEADERS)
gt = resp.cookies.get_dict().get("gt") or "".join(re.findall(r'(?<=\"gt=)[^;]+', resp.text))

print(gt)
headers = {
    'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs'
                     '%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    'x-guest-token': f'{gt}',
}

params = {
    'variables': '{"userId":"44196397","count":20,"includePromotedContent":true,'
                 '"withQuickPromoteEligibilityTweetFields":true,"withVoice":true,"withV2Timeline":true}',
    'features': '{"responsive_web_graphql_exclude_directive_enabled":true,"verified_phone_label_enabled":false,'
                '"creator_subscriptions_tweet_preview_api_enabled":true,'
                '"responsive_web_graphql_timeline_navigation_enabled":true,'
                '"responsive_web_graphql_skip_user_profile_image_extensions_enabled":false,'
                '"c9s_tweet_anatomy_moderator_badge_enabled":true,"tweetypie_unmention_optimization_enabled":true,'
                '"responsive_web_edit_tweet_api_enabled":true,'
                '"graphql_is_translatable_rweb_tweet_is_translatable_enabled":true,'
                '"view_counts_everywhere_api_enabled":true,"longform_notetweets_consumption_enabled":true,'
                '"responsive_web_twitter_article_tweet_consumption_enabled":true,'
                '"tweet_awards_web_tipping_enabled":false,"freedom_of_speech_not_reach_fetch_enabled":true,'
                '"standardized_nudges_misinfo":true,'
                '"tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled":true,'
                '"rweb_video_timestamps_enabled":true,"longform_notetweets_rich_text_read_enabled":true,'
                '"longform_notetweets_inline_media_enabled":true,"responsive_web_enhance_cards_enabled":false}',
}

response = requests.get(
    'https://api.twitter.com/graphql/eS7LO5Jy3xgmd3dbL044EA/UserTweets',
    params=params,
    headers=headers,
)


print(response)
json_response = response.json()

tweets = []

result = json_response.get("data", {}).get("user", {}).get("result", {}).get("timeline_v2", {}).get("timeline", {}).get("instructions", [])


object_1 = result[1].get("entry", {}).get("content", {}).get("itemContent", {}).get("tweet_results", {}).get("result", {}).get("legacy", {})
tweets.append(object_1.get("full_text"))
object_2 = result[2].get("entries", [])
for tweet in object_2[:11]:
    text = tweet.get("content", {}).get("itemContent", {}).get("tweet_results", {}).get("result", {}).get("legacy", {})
    tweets.append(text["full_text"])

print(tweets)

with open('logfile.txt', 'w') as log_file:
    for twit_text in tweets:
        log_file.write(twit_text + '\n')