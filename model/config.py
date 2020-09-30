sms_market_url = 'https://private-anon-2815855b50-smsmarket.apiary-proxy.com/webservice-rest/mt_date?user=fssmsmarket&password=s3nh%40123%40%21%40&start_date={}&end_date={}&type=0&status=0%2C1&timezone=-03%3A00'

sms_market_status = {'-2': 'Erro de rede da operadora',
                       '1': 'Mensagem recebida pelo dispositivo',
                       '9': 'Mensagem não recebida pelo dispositivo',
                       '-9': 'Bloqueado - Sem Cobertura',
                       '-8': 'Bloqueado - Conteúdo não permitido',
                       '-6': 'Mensagem cancelada com sucesso',
                       '-5': 'Bloqueado - Lista de bloqueio',
                       '-4': 'Bloqueado - Número fixo',
                       '-3': 'Bloqueado - Número inválido',
                       '0': 'Mensagem recebida pela operadora',
                       '7': 'Mensagem expirada pela operadora',
                       '8': 'Mensagem rejeitada pela operadora',
                       '-1': 'Mensagem na fila',
                       '3': 'Preparando mensagem para enviar',
                       '6': 'Mensagem Pausada'
                       }