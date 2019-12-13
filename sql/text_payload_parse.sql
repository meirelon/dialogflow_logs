with
textpayload_split as(
select split(textPayload, '"') as x, labels.request_id
from `scarlet-labs.stackdriver.dialogflow_agent`
where textPayload like 'Dialogflow Response%' and labels.type = 'dialogflow_response'
)

select
timestamp(x[offset(7)]) as time,
request_id,
x[offset(5)] as session_id,
x[offset(11)] as user_text,
x[offset(31)] as response,
x[offset(3)] as lang,
x[offset(13)] as action,
x[offset(21)] as intent_id,
x[offset(23)] as intent_name,
x[offset(29)] as is_fallback_intent
from textpayload_split
where x[offset(21)] not in ('success', 'false')
