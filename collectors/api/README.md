# Intake API/HEC
Les JSONL simulent les réponses d'une API. Concevoir un poller avec pagination `nextLink`, checkpoint durable, retry exponentiel/jitter, traitement de 429/5xx, déduplication via `event_id`, métriques fetched/sent/rejected/retried et token via variable d'environnement. Ne jamais commiter un token.
