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
.............

<li>**Nume Request n**</li>

HTTP method for request: **Inserati aici metoda HTTP a requestului**<br>
Request description: **Inserati o scurta descriere a requestului, conform documentatiei de API**<br>
Test types / techniques used: **Inserati tipurile si tehnicile de testare folosite pentru acest request**<br>
Response status code: **Inserati aici status code-ul pe care l-ati obtinut in urma executiei requestului**<br>

Below you can find a picture of the API request from Postman:<br>

**Inserati aici o poza cu requestul din postman in care sa se observe request method, endpoint, request body si response body**<br>

JavaScript Tests:

**Inserati aici o poza cu testele in java script pe care le-ati definit impreuna cu rezultatele executiei acestora**<br>

</ol>

<h2>Execution report for the created API collection </h2>

Below you can find the execution report that was generated through the Postman collection runner. <br>

**Inserati aici o poza cu raportul de executie din Postman**<br>

The collection was also run through newman directly from the terminal, and the results can be found below:<br>

**Inserati aici o poza cu raportul de executie din Newman**<br>

<h2>Defects found</h2>

The following issues were identified while running the postman tests:<br>

****Inserati aici fie un fisier pdf care sa contina raportarea tuturor bug-urilor, fie le descrieti direct in git
Bug-urile trebuie sa contina titlu, preconditii, pasi de executie, rezultate asteptate si rezultate actuale.
Optional, bug-urile pot fi raportate in jira, si apoi puteti pune poze direct din jira**

<h2>Conclusions</h2>

**Inserati aici concluziile pe care le-ati obtinut in urma executarii testelor  si introduceti informatii cum ar fi cate teste au fost create si executate, ce procentaj aproximativ din cerintele in scop au fost acoperite, daca exista vreo functionalitate pe care nu ai apucat sa o testezi, daca bug-urile gasite impacteaza lansarea produsului in productie sau se pot fixa si ulterior, daca ai identificat riscuri de produs care trebuie mitigate, daca e vreo reecomandare pe care vrei sa o faci pentru lansare, daca sunt ceva lessons learned de care trebuie sa se tina cont la proiectele viitoare etc**


