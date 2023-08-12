from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
from gql.dsl import Query

# 设置GraphQL端点的URL
transport = RequestsHTTPTransport(url="https://your-graphql-endpoint-url.com")

# 创建GraphQL客户端
client = Client(transport=transport, fetch_schema_from_transport=True)

# 使用QueryBuilder构建查询
query = Query(items={"name": "m855a1"}).select("id", "name", "shortName")

# 将QueryBuilder对象转换为GraphQL查询对象
gql_query = gql(query)

# 使用查询对象进行查询
result = client.execute(gql_query)

# 打印查询结果
print(result)
