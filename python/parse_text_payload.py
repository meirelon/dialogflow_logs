# import Pubsub package
# import way to stream to BQ

def parse_text(text_payload):
    """
    EXAMPLE:


    Dialogflow Response : id: "xxx"
    lang: "en"
    session_id: "xxx"
    timestamp: "2019-12-12T04:46:17.644Z"
    result {
      source: "agent"
      resolved_query: "hello?"
      action: "input.welcome"
      score: 1.0
      parameters {
      }
      contexts {
        name: "__system_counters__"
        lifespan: 1
        parameters {
          fields {
            key: "no-input"
            value {
              number_value: 0.0
            }
          }
          fields {
            key: "no-match"
            value {
              number_value: 0.0
            }
          }
        }
      }
      metadata {
        intent_id: "xxx"
        intent_name: "Default Welcome Intent"
        webhook_used: "false"
        webhook_for_slot_filling_used: "false"
        is_fallback_intent: "false"
      }
      fulfillment {
        speech: "Good day! What can I do for you today?"
        messages {
          lang: "en"
          type {
            number_value: 0.0
          }
          speech {
            string_value: "Good day! What can I do for you today?"
          }
    """



    lang=[]
    session_id = []
    timestamp = []
    resolved_query = []
    action = []
    intent_id = []
    intent_name = []
    is_fallback_intent = []
    speech = []

    text_payload_split = [x.strip() for x in text_payload.split('"')]

    for i in range(1, len(text_payload_split)):
        # lang
        if "lang" in text_payload_split[i-1]:
            lang.append(text_payload_split[i])

        # session_id
        if "session_id" in text_payload_split[i-1]:
            session_id.append(text_payload_split[i])

        # timestamp
        if "timestamp" in text_payload_split[i-1]:
            timestamp.append(text_payload_split[i])

        # resolved_query
        if "resolved_query" in text_payload_split[i-1]:
            resolved_query.append(text_payload_split[i])

        # action
        if "action" in text_payload_split[i-1]:
            action.append(text_payload_split[i])

        # intent_id
        if "intent_id" in text_payload_split[i-1]:
            intent_id.append(text_payload_split[i])

        # intent_name
        if "intent_name" in text_payload_split[i-1]:
            intent_name.append(text_payload_split[i])

         # is_fallback_intent
        if "is_fallback_intent" in text_payload_split[i-1]:
            is_fallback_intent.append(text_payload_split[i])

        # speech
        if "speech" in text_payload_split[i-1]:
            speech.append(text_payload_split[i])

        text_payload_list = [lang,
                             session_id,
                             timestamp,
                             resolved_query,
                             action,
                             intent_id,
                             intent_name,
                             is_fallback_intent,
                             speech]
        text_payload_keys = ["lang",
                             "session_id",
                             "timestamp",
                             "resolved_query",
                             "action",
                             "intent_id",
                             "intent_name",
                             "is_fallback_intent",
                             "speech"]
        text_payload_dict = {text_payload_keys[i]: text_payload_list[i][0] for i in range(len(text_payload_keys))}

        return text_payload_dict
