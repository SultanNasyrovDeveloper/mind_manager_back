# Palace Node Application

## Schemas

### Node Media
### Node Tag
### Node Body
### Node
| Field           | Type                   | Description                              |
|-----------------|------------------------|------------------------------------------|
| **id**          | Integer                | Unique id of node.                       |
| **owner**       | Integer                | Id of user that owns this node.          |
| **parent**      | Integer                | Id of a parent node. Can be null only if |
| **name**        | String                 |                                          |
| **description** | String                 |                                          |
| **tags**        | Tag[]                  |                                          |
| **ancestors**   | Integer[]              |                                          |
| **statistics**  | NodeLearningStatistics |                                          |
| **media**       | Media[]                |                                          |
| **body**        | NodeBody               |                                          |
| **children**    | Integer[]              |                                          |

## API
### GET /api/v1/palace/nodes/
#### Query Params

Fetch list of nodes