## Learning Session Application
Learning session contains information about one particular user practice session on mind palace.
Uses learning strategy to perform learning related methods. User may have only one active 
session at the time. Session can expire if no repetition were performed in a certain amount of time
specified in application settings.

### Schemas:

#### LearningSession
##### is_active
Defines whether learning session is active.
##### user
User of learning session.
##### strategy_name
Name of strategy that will perform some learning related
actions like
##### targets 

##### queue
Contains ordered node to perform repetition on. Application has a list of common queue generation algorithms
or can delegate work to learning strategy. When queue is empty session is over.
User can generate new queue or finish current learning session.
##### additional_queue
Contains ordered list of nodes that can be repeated after main queue. Learning session or learning strategies
can put nodes here for example if user repetition rating was low and nodes need to be repeated. 
##### repeated_nodes
List of minda palace nodes tha were repeated. For now, 
emulates repetition storage.

##### start_timestamp
Contains learning session start timestamp as datetime
##### end_timestamp
Contains learning session end timestamp as datetime
##### last_repetition_timestamp
Contains learning session last repetition timestamp as datetime


#### LearningSessionStatistics
##### session
##### average_rating
##### total_repetitions

### API
#### create
Check and close all expired user sessions. Check if active user session already exists.
If active session exists raise ActiveSessionAlreadyExistsError. 
Generates learning queue and creates new learning session statistics with empty values. 
Learning session has targets which are mind palace nodes. Target node's children will be used
to populate learning queue. Session target can be added but can not be deleted after.

#### fetch active session
Performs query to fetch all active user learning sessions.
If more than 1 close all except the latest one. 
If session is expired raise SessionExpiredError.
Else return learning session.

#### fetch learning session detail
Fetch session. If session expired finish it. 
Return session.

#### start learning session

#### fetch learning sessions list
Fetch paginated list of learning session objects.

#### add learning target
Adds target to learning session and regenerates queue.

#### generate learning queue
Generates learning session queue according to queue generation parameters.
Learning session may use learning strategy to generate queue.

#### record_repetition
Handle node repetition. For now, this endpoint just changes statistics of node and 
learning session. Later repetitions will be stored in separate clickhouse database.

#### finish session
Finish learning session. Learning session will be deleted if no nodes were repeated.

#### Exceptions
SessionExpiredError  
This action can not be performed because your learning session expired. 
Start new learning session to continue learning.
