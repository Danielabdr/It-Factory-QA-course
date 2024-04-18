<h1>API Testing Project for TMDB(The Movie Database)</h1>

The scope of this project is to use all  API knowledge gained throught the Software Testing course and apply them in practice, using a live application.

Application under test: TMDB (The Movie Database) v4

Tools used: Postman, Newman

Collection link: **Inserati aici linkul catre colectia de API**

<h2>Tests performed</h2>

<ol>
<li>Request token</li>

HTTP method for request: POST <br>
Request description: 
This method generates a new request token that you can ask a user to approve. This is the first step in getting permission from a user to read and write data on their behalf.<br>
Test types / techniques used: Positive testing<br>
Response status code: 200 <br>

Below you can find a picture of the API request from Postman:<br>

![request token](https://github.com/Danielabdr/It-Factory-QA-course/assets/157109953/3435b983-8291-4392-8e4f-756ca7da70f9)<br>

<li>Ask permission</li>

HTTP method for request: POST <br>
Request description: Create an intermediate request token that can be used to validate a TMDB user login.<br>
Test types / techniques used: Positive testing <br>
Response status code: 200 <br>

<li>Create Access Token</li>

HTTP method for request: POST <br>
Request description: This method will finish the user authentication flow and issue an official user access token. The request token in this request is sent along as part of the POST body. You should still use your standard API read access token for authenticating this request.<br>
Test types / techniques used: Positive testing <br>
Response status code: 200 <br>

Below you can find a picture of the API request from Postman:<br>

![access token](https://github.com/Danielabdr/It-Factory-QA-course/assets/157109953/19fb1c96-e1fa-4559-8a9a-e685bbe19acd)
<br>

<li>GET account list</li>

HTTP method for request: GET <br>
Request description: Get all of the lists you've created.<br>
Test types / techniques used: Positive testing <br>
Response status code: 200 <br>

Below you can find a picture of the API request from Postman:<br>

![get account list](https://github.com/Danielabdr/It-Factory-QA-course/assets/157109953/e2bfcb23-23c4-4c61-8b35-6108811bff85)
<br>

<li>GET favorite movies</li>

HTTP method for request: GET <br>
Request description: Get a user's list of favourite movies.<br>
Test types / techniques used: Positive testing <br>
Response status code: 200 <br>

Below you can find a picture of the API request from Postman:<br>

![get favorite movies](https://github.com/Danielabdr/It-Factory-QA-course/assets/157109953/9a63f6e7-ffaa-4166-a938-3d3d3254a8bd)

<br>

<li>GET list details</li>

HTTP method for request: GET <br>
Request description: Retrieve a list by id.Private lists can only be accessed by their owners and therefore require a valid user access token.<br>
Test types / techniques used: Positive testing <br>
Response status code: 200 <br>

Below you can find a picture of the API request from Postman:<br>

![get list details](https://github.com/Danielabdr/It-Factory-QA-course/assets/157109953/1329f2a3-dbe9-49e9-a41c-8e8a9d36f023)
<br>

JavaScript Tests:<br>
![l det test](https://github.com/Danielabdr/It-Factory-QA-course/assets/157109953/16583463-46c9-4ff2-a93a-870da78f4781)<br>
![det l test](https://github.com/Danielabdr/It-Factory-QA-course/assets/157109953/7b3be7f8-8ef1-436d-a3ca-9163115652b1)<br>
![sds](https://github.com/Danielabdr/It-Factory-QA-course/assets/157109953/20b001c5-60ed-481c-9d9a-301c90f7eab1)<br>


<li>GET list details-Negative testing with unexisting list id</li>

HTTP method for request: GET <br>
Request description: Retrieve a list by id.Private lists can only be accessed by their owners and therefore require a valid user access token.<br>
Test types / techniques used: Positive testing <br>
Response status code: 404 <br>

Below you can find a picture of the API request from Postman:<br>

![sdcdssd](https://github.com/Danielabdr/It-Factory-QA-course/assets/157109953/97a1a65a-0741-48e7-a67b-3350c273feab)<br>

JavaScript Tests:<br>
![erdgr](https://github.com/Danielabdr/It-Factory-QA-course/assets/157109953/5ca1e18f-012b-49cd-bb61-5219e4ccee67)<br>
![sadssd](https://github.com/Danielabdr/It-Factory-QA-course/assets/157109953/81fa9e4b-72cf-4875-9a48-cff0eee63c09)<br>


<li>Add item to a list</li>

HTTP method for request: POST <br>
Request description: Add items to a list.<br>
Test types / techniques used: Positive testing <br>
Response status code: 200 <br>

Below you can find a picture of the API request from Postman:<br>

![mn nm nm](https://github.com/Danielabdr/It-Factory-QA-course/assets/157109953/23b12f90-3b5b-4ea7-8884-4fedb131956d)<br>

JavaScript Tests:<br>
![tests](https://github.com/Danielabdr/It-Factory-QA-course/assets/157109953/8739c81f-db46-4faf-bd8d-0f39c7b162d6)<br>
![sdfsdf](https://github.com/Danielabdr/It-Factory-QA-course/assets/157109953/f892cb5a-b81c-4445-9e7c-6281cca5198c)<br>
![zxczzx](https://github.com/Danielabdr/It-Factory-QA-course/assets/157109953/994dded9-c2c2-491d-8b3d-2e3b49d5fc2a)<br>

<li>Add items to a list-Negative testing with null parameter values in body params</li>

HTTP method for request: POST <br>
Request description: Add items to a list.<br>
Test types / techniques used: Negative testing <br>
Response status code: 200 <br>

Below you can find a picture of the API request from Postman:<br>

![sdvfsdvsdv](https://github.com/Danielabdr/It-Factory-QA-course/assets/157109953/06007239-dc9e-46d6-bf3d-536404a46c57)<br>

JavaScript Tests:<br>
![sdfsdfsdfsd](https://github.com/Danielabdr/It-Factory-QA-course/assets/157109953/e5219d50-6f54-4bcc-a031-ab1fd076412e)<br>

<li>Add item to a list-Negative testing with unexisting movie id in body params</li>

HTTP method for request: POST <br>
Request description: Add items to a list.<br>
Test types / techniques used: Negative testing <br>
Response status code: 200 <br>

Below you can find a picture of the API request from Postman:<br>

![sds](https://github.com/Danielabdr/It-Factory-QA-course/assets/157109953/86154221-2686-4bb5-91bd-c3b8b2d4f81f)<br>

JavaScript Tests:<br>
![xdcdsxvd](https://github.com/Danielabdr/It-Factory-QA-course/assets/157109953/4ab8738c-412f-4ec9-b982-5320d33253ec)<br>

<li>Add items to a list-Negative testing with unexisting media type value in body params</li>

HTTP method for request: POST <br>
Request description: Add items to a list.<br>
Test types / techniques used: Negative testing <br>
Response status code: 200 <br>

Below you can find a picture of the API request from Postman:<br>

![sdfsdfsd](https://github.com/Danielabdr/It-Factory-QA-course/assets/157109953/472bb2fe-7a72-4214-99d9-2552710cb4a2)<br>

JavaScript Tests:<br>
![dvsdvsdv](https://github.com/Danielabdr/It-Factory-QA-course/assets/157109953/f8bad5de-3b07-4070-bedd-10a6aba07a3b)<br>

<li>Clear all the items of the list</li>

HTTP method for request: GET <br>
Request description: Clear all of the items on a list.<br>
Test types / techniques used: Positive testing <br>
Response status code: 200 <br>

Below you can find a picture of the API request from Postman:<br>

![zxcsdzcd](https://github.com/Danielabdr/It-Factory-QA-course/assets/157109953/8236feef-b299-4752-bf9f-3828a00de095)<br>

JavaScript Tests:<br>
![sddsfdsf](https://github.com/Danielabdr/It-Factory-QA-course/assets/157109953/8a7c88ae-b928-4436-85e5-3003c17b6d4a)<br>

<li>Create list</li>

HTTP method for request: POST<br>
Request description: Create a new list.<br>
Test types / techniques used: Positive testing <br>
Response status code: 200 <br>

Below you can find a picture of the API request from Postman:<br>

![mn mnm,n](https://github.com/Danielabdr/It-Factory-QA-course/assets/157109953/1e50c6a0-43d5-4a48-83e5-9e8da80317a0)<br>

JavaScript Tests:

![t1](https://github.com/Danielabdr/It-Factory-QA-course/assets/157109953/f026b0ed-cf3c-4fd4-b935-53ef49b63be4)<br>
![t2](https://github.com/Danielabdr/It-Factory-QA-course/assets/157109953/ce968979-0f36-4dde-8bd7-69e0628ec77a)<br>

<li>Create list-Negative testing with null body parameter values</li>

HTTP method for request: POST <br>
Request description:Create a new list.<br>
Test types / techniques used: Negative testing <br>
Response status code: 400 <br>

Below you can find a picture of the API request from Postman:<br>

![,mnknmkn](https://github.com/Danielabdr/It-Factory-QA-course/assets/157109953/298b55db-2b32-456a-bdfb-ab1d640f222b)<br>

JavaScript Tests:

![mnbnbn](https://github.com/Danielabdr/It-Factory-QA-course/assets/157109953/e62e5b47-a88b-48c0-9d38-9a7652e079a8)<br>

<li>Check if an item is on a list</li>

HTTP method for request: GET <br>
Request description: Check if an item is on a list.<br>
Test types / techniques used: Positive testing <br>
Response status code: 200 <br>

Below you can find a picture of the API request from Postman:<br>

![kjhjkjk](https://github.com/Danielabdr/It-Factory-QA-course/assets/157109953/60b90b48-4a64-4ccb-bc98-5eb2178907e7)<br>

<li>Check if an unexisting item is on a list-Negative testing</li>

HTTP method for request: GET <br>
Request description: Check if an item is on a list.<br>
Test types / techniques used: Negative testing <br>
Response status code: 404 <br>

Below you can find a picture of the API request from Postman:<br>

![mbnjknkj](https://github.com/Danielabdr/It-Factory-QA-course/assets/157109953/bb557ad6-f336-42f8-a4b0-e352ecf0808d)<br>

JavaScript Tests:

![nbnbjn](https://github.com/Danielabdr/It-Factory-QA-course/assets/157109953/fbc57dc0-0966-46d3-b74b-778f5304ca99)<br>


<li>Update the details of a list</li>

HTTP method for request: PUT <br>
Request description: Update the details of a list.<br>
Test types / techniques used: Positive testing<br>
Response status code: 201 <br>

Below you can find a picture of the API request from Postman:<br>

![,mnkmn](https://github.com/Danielabdr/It-Factory-QA-course/assets/157109953/50248fb7-1ad2-4d0e-a206-246d61955daf)<br>

<li>Update the details of an unexisting list</li>

HTTP method for request: PUT <br>
Request description: Update the details of a list.<br>
Test types / techniques used: Negative testing <br>
Response status code: 201 <br>

Below you can find a picture of the API request from Postman:<br>

![knkjnkjnj](https://github.com/Danielabdr/It-Factory-QA-course/assets/157109953/35992ba7-cdab-4b0c-9dcb-77642cf7e72c)<br>

JavaScript Tests:

![image](https://github.com/Danielabdr/It-Factory-QA-course/assets/157109953/0b1364f3-0a71-45bc-ad94-3edc98652d74)<br>

<li>Remove items from list</li>

HTTP method for request: DELETE <br>
Request description: Removes items from a list.<br>
Test types / techniques used: Positive testing <br>
Response status code: 200 <br>

Below you can find a picture of the API request from Postman:<br>

![lkmklmkl](https://github.com/Danielabdr/It-Factory-QA-course/assets/157109953/c8e7f693-bcce-4b8f-99fd-53a9fc495d9d)<br>



.............

</ol>

<h2>Execution report for the created API collection </h2>

Below you can find the execution report that was generated through the Postman collection runner. <br>

![re1](https://github.com/Danielabdr/It-Factory-QA-course/assets/157109953/5263b1ba-6e10-469a-8c1f-7a772f6a718f)<br>
![re2](https://github.com/Danielabdr/It-Factory-QA-course/assets/157109953/821bd803-4875-4b00-bf42-57050c8f330d)<br>
![re3](https://github.com/Danielabdr/It-Factory-QA-course/assets/157109953/2c00dc56-0fdd-4fe2-bf17-3cd78329e56d)<br>
![re4](https://github.com/Danielabdr/It-Factory-QA-course/assets/157109953/aa8a60cc-7fe1-4c26-86ea-5cb1062258d0)<br>

The collection was also run through newman directly from the terminal, and the results can be found below:<br>

![n1](https://github.com/Danielabdr/It-Factory-QA-course/assets/157109953/410329b2-019e-4c3f-8ba5-56fda8932c07)<br>
![n2](https://github.com/Danielabdr/It-Factory-QA-course/assets/157109953/44dc35f5-b3f7-44e4-9a5a-2a798809519e)<br>
![n3](https://github.com/Danielabdr/It-Factory-QA-course/assets/157109953/2e0a4eaf-c1a5-445a-8a29-2c2062b2e2b8)<br>
![n4](https://github.com/Danielabdr/It-Factory-QA-course/assets/157109953/a49848b6-6ec9-4b4f-a07c-7ebd34c19e3d)<br>

<h2>Defects found</h2>

The following issues were identified while running the postman tests:<br>

<h3>Bug 1</h3>

The user should not be able to add items to a list with null values in body parameters

Steps to reproduce:
*	Open Postman application
* Click on „New” button from the top-left corner of the page
* Click on „HTTP” icon 
* Enter endpoint request  https://api.themoviedb.org/4/list/{list_id}/items
* Replace „{list_id}” with the list id in wich you want to add the items
* Add HTTP method for the request (POST)
* Click on „Body”  Raw and insert the following body params:
{
  "items": [
    {
      "media_type": null,
      "media_id": null
    }
  ]
}
* Click on „Headers”  Add new key field with „Authorization” text and Authorization token on value field ((Ex: „Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NWFmZTNlMzY3YjYxMzAwYWZmMGFiODciLCJuYmYiOjE3MDg0MzkwMDEsImF1ZCI6IjhhNjU3MTQwNzk5OTQwNDMwYjQ5MzY1NTBhOTUwNjUzIiwianRpIjoiNjc0MjUwNiIsInNjb3BlcyI6WyJhcGlfcmVhZCIsImFwaV93cml0ZSJdLCJ2ZXJzaW9uIjoxfQ.24I44CN46rLJglDrlajkH7q0EFHiaeQH6ut0ClcLDyA”)  
* Click „Send” button

Expected results: The user should not be able to add items on the list and an error message should be returned with the 404 status code.

Actual results: The returned status code is 200 instead of 404 and an error message is returned in the response body saying "Media is required".

<h3>Bug 2</h3>

The user should not be able to add items to a list with unexisting movie id in body params

Steps to reproduce:
* Open Postman application
* Click on „New” button from the top-left corner of the page
* Click on „HTTP” icon
* Enter endpoint request  https://api.themoviedb.org/4/list/{list_id}/items
* Replace „{list_id}” with the list id in wich you want to add the items
* Add HTTP method for the request (POST)
* Click on „Body”  Raw and insert the following body params:
{
  "items": [
    {
      "media_type": "movie",
      "media_id": 56889623163
    }
  ]
}
* Click on „Headers”  Add new key field with „Authorization” text and Authorization token on value field ((Ex: „Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NWFmZTNlMzY3YjYxMzAwYWZmMGFiODciLCJuYmYiOjE3MDg0MzkwMDEsImF1ZCI6IjhhNjU3MTQwNzk5OTQwNDMwYjQ5MzY1NTBhOTUwNjUzIiwianRpIjoiNjc0MjUwNiIsInNjb3BlcyI6WyJhcGlfcmVhZCIsImFwaV93cml0ZSJdLCJ2ZXJzaW9uIjoxfQ.24I44CN46rLJglDrlajkH7q0EFHiaeQH6ut0ClcLDyA”)
* Click „Send” button

Expected results: The user should not be able to add items on the list and an error message should be returned with the 404 status code.

Actual results: The returned status code is 200 instead of 404 and an error message is returned in the response body saying "Media is required".

<h3>Bug 3</h3>

The user should not be able to add items to a list unexisting media type value in body params

Steps to reproduce:
* Open Postman application
* Click on „New” button from the top-left corner of the page
* Click on „HTTP” icon
* Enter endpoint request  https://api.themoviedb.org/4/list/{list_id}/items
* Replace „{list_id}” with the list id in wich you want to add the items
* Add HTTP method for the request (POST)
* Click on „Body”  Raw and insert the following body params:
{
  "items": [
    {
      "media_type": "bvvjbjn b",
      "media_id": 1072790
    }
  ]
}
*	Click on „Headers”  Add new key field with „Authorization” text and Authorization token on value field ((Ex: „Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NWFmZTNlMzY3YjYxMzAwYWZmMGFiODciLCJuYmYiOjE3MDg0MzkwMDEsImF1ZCI6IjhhNjU3MTQwNzk5OTQwNDMwYjQ5MzY1NTBhOTUwNjUzIiwianRpIjoiNjc0MjUwNiIsInNjb3BlcyI6WyJhcGlfcmVhZCIsImFwaV93cml0ZSJdLCJ2ZXJzaW9uIjoxfQ.24I44CN46rLJglDrlajkH7q0EFHiaeQH6ut0ClcLDyA”)
*	Click „Send” button

Expected results: The user should not be able to add items on the list and an error message should be returned with the 404 status code.

Actual results: The returned status code is 200 instead of 404 and an error message is returned in the response body saying "Media is required".

<h3>Bug 4</h3>

The user should not be able to create a list

Steps to reproduce:
* Open Postman application
* Click on „New” button from the top-left corner of the page
* Click on „HTTP” icon
* Enter endpoint request  https://api.themoviedb.org/4/list
* Add HTTP method for the request (POST)
* Click on „Body”  Raw and insert the following body params:
{
  "description": "",
  "name": "My first created Listtttt",
  "iso_3166_1": "US",
  "iso_639_1": "en",
  "public": true
}
* Click on „Headers”  Add new key field with „Authorization” text and Authorization token on value field ((Ex: „Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NWFmZTNlMzY3YjYxMzAwYWZmMGFiODciLCJuYmYiOjE3MDg0MzkwMDEsImF1ZCI6IjhhNjU3MTQwNzk5OTQwNDMwYjQ5MzY1NTBhOTUwNjUzIiwianRpIjoiNjc0MjUwNiIsInNjb3BlcyI6WyJhcGlfcmVhZCIsImFwaV93cml0ZSJdLCJ2ZXJzaW9uIjoxfQ.24I44CN46rLJglDrlajkH7q0EFHiaeQH6ut0ClcLDyA”)  
* Click „Send” button

Expected results: The user should be able to create the list and a success message should be returned with 200 status code.

Actual results: The returned status code is 201 instead of 200.



 


<h2>Conclusions</h2>

Here's a summary of the test results:

* A total of 19 test requests were created and executed.
* There were no errors encountered during the execution of any test.
* 12 test scripts were executed, with 29 assertions in total.
* All requests received responses within an acceptable time frame, with an average of around 238ms.

Conclusions:

* Some errors were identified and successfully addressed, such as verifying response status codes in certain negative scenarios.
* There are some test cases that were not covered or could be expanded to include more scenarios.
* The identified bugs could have a negative impact on the production release and should be addressed before deployment.
* The recommendation for release would be to perform an additional review of tests and address all identified bugs.
* Product risks should be evaluated and mitigated before release to minimize their impact on the end-user experience.
* It's important to take the lessons learned from this testing round and apply them to future projects to improve the testing process and product quality.
In conclusion, while some issues were identified, the testing process was generally successful and provided a solid foundation for the production release. Continued monitoring and improvement of product quality are important as the product evolves.
