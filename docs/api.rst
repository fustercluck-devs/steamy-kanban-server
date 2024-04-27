=========
API
=========


.. http:get:: /v1/steamfacade/appdetails?appids={app_id}

   Get the app details for an app id from steam api

   **Example request**:

   .. sourcecode:: http

      GET /v1/steamfacade/appdetails?appids=1328670 HTTP/1.1

   **Example successful response**:

   .. sourcecode:: http
        
      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: application/json
   .. literalinclude:: ./steam_resp_1328670.json
   :language: JSON


   **Example unsuccessful response**:

   .. sourcecode:: http
        
      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: application/json
      
   .. literalinclude:: ./steam_resp_1328670_unsuccessful.json
   :language: JSON


   :query appids: The steam app id of each item to retrieve
   :reqheader Accept: application/json
   :statuscode 200: app details successfully retrieved
