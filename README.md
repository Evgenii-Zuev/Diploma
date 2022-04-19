# Diploma task

Create a simple Web-application (see the description in the “Application” section below), CI/CD infrastructure and pipeline for it.
Создайте простое Web-приложение (см. описание в разделе "Приложение" ниже), инфраструктуру CI/CD и конвейер для него.
# Acceptance Criteria and presentation
A short presentation (.ppt or other) which contains description of the solution should be prepared and sent to the commission before a demo session. 
Короткая презентация (.ppt или другая ), содержащая описание решения, должна быть подготовлена и отправлена в комиссию до демонстрационной сессии.

The working application with the pipeline is to be demonstrated live on a “protection of the diploma” session for experts with comments and explanation of the details of the implementation, reasons of choosing tools and technologies. 
Работающее приложение с конвейером будет продемонстрировано в прямом эфире на сессии «Защита диплома» для экспертов с комментариями и разъяснением деталей внедрения, причин выбора инструментов и технологий.

Detailed requirements/criteria: 
Подробные требования/критерии:

|**Criteria**|**Reqiurements**|**Related Module**|
| :-: | :-: | :-: |
|**SCM**|Application sources should be placed in Git repository. Branching strategy should be explained. <br>Исходные коды приложений должны быть размещены в репозитории Git. Стратегия ветвления должна быть объяснена.|Git|
|**Tests\***|CI pipeline may contain unit tests, smoke tests, linter check. Трубопровод CI может содержать модульные тесты, дымовые тесты, проверку линтера.|CI/CD|
|**Quality gate**|CI/CD pipeline should use some quality/vulnerability control tool like a Sonar or Anchore. <br>Конвейер CI/CD должен использовать какой-то инструмент контроля качества/уязвимостей, такой как Sonar или Anchore.|CI/CD|
|**IaC**|CI/CI and runtime infrastructure should be described as a code using Terraform, CloudFormation, or any similar tool. On the demonstration deployment procedure should be shown. <br>CI/CI и инфраструктура среды выполнения должны быть описаны как код, использующий Terraform, CloudFormation или любой подобный инструмент. На демонстрации должна быть показана процедура развертывания.|Cloud, Terraform, Ansible|
|**Orchestration**|All non cloud-native tools should be spinned up inside a K8S/OpenShift cluster inside a cloud. Application runtime environments should be inside the cluster too. <br>Все необлачные инструменты должны быть раскручены внутри кластера K8S/OpenShift внутри облака. Среды выполнения приложений также должны находиться внутри кластера.|Kubernetes|
|**Logging**|Infrastructure should have centralized log collection/display system. Logs of the application components and infra components should be collected. <br>Инфраструктура должна иметь централизованную систему сбора/отображения журналов. Необходимо собрать журналы компонентов приложения и инфракомпонентов.|Monitoring and Logging|
|**Monitoring**|Infrastructure should have centralized metric collection/display system. Metrics of the application components and infra components should be collected. <br>Инфраструктура должна иметь централизованную систему сбора/отображения метрик. Необходимо собрать метрики компонентов приложения и инфракомпонентов.|<p>Monitoring and Logging</p><p></p>|
|**Runtime/Deployment**|Runtime infrastructure should have production and non production environments.  Deploy/release strategy should be explained. Инфраструктура среды выполнения должна иметь производственные и непроизводственные среды. Следует разъяснить стратегию развертывания/выпуска.|CI/CD|
|**Scalability/redundancy**|Scalability should be provided and demonstrated<br>Масштабируемость должна быть обеспечена и продемонстрирована|Kubernetes|
|**Cloud and Cost efficiency\*\***|<p>Cloud resources and services must be used for the task. Report about the Cloud resource usage and the cost must be provided in the presentation. It should be efficient (minimal) – in accordance to the solving tasks. You can choose any cloud provider taking into account possible extra costs for the resources. Для выполнения задачи необходимо использовать облачные ресурсы и службы. Отчет об использовании облачных ресурсов и стоимости должен быть предоставлен в презентации. Она должна быть эффективной (минимальной) – в соответствии с поставленными задачами. Вы можете выбрать любого облачного провайдера с учетом возможных дополнительных затрат на ресурсы.</p><p></p>|Cloud|
*\* Nice to have – optional*

*\*\* Be careful with the Cloud resource usage and check the costs for not to exceed limits! Switch off your machines when you are not using them!*
# Application
Develop a simple (lightweight) 3-tire application (front-end, back-end, database).
` `Разработайте простое (легкое) приложение с 3 шинами (front-end, back-end, database)

Back-end (collects data) must:

\1. Retrieve a portion of data from API (see in your Variant) and store it in a database
Извлеките часть данных из API (см. в вашем варианте) и сохраните их в базе данных

\2. Update data on demand
Обновление данных по запросу

\3. Update DB schema if needed on app’s update
При необходимости обновите схему БД при обновлении приложения

Front-end (outputs data) must: 
Интерфейс (выходные данные) должен

\1. Display any portion of the data stored in the DB
Отображение любой части данных, хранящихся в БД

\2. Provide a method to trigger data update process
Предоставьте метод запуска процесса обновления данных

Database:

\1. Choose Database type and data scheme in a suitable manner. 
Выберите тип базы данных и схему данных подходящим образом 

\2. Data must be stored in a persistent way
Данные должны храниться постоянным образом

\3. It’s better to use cloud native DB solutions like an RDS/AzureSQL/CloudSQL.
` `Лучше использовать облачные решения для баз данных, такие как RDS/AzureSQL/CloudSQL.

**You’ll get your Variant of the application individually.**

**Вариант 2. Используя API https://affiliate.itunes.apple.com/resources/documentation/itunes-store-web-service-search-api/ получить все данные о "The Beatles" и сохранить их в своей БД: kind, collectionName, trackName, collectionPrice, trackPrice, primaryGenreName, trackCount, trackNumber, releaseDate. Выводите данные по collectionName (задается имя коллекции) в виде таблицы и сортируйте их по releaseDate в порядке возрастания.**



Напомню, что он имеет статус дипломного задания, которое демонстрирует успешность вашего окончания курса. Настоятельно рекомендуется выполнять его во время обучения (рекомендуемые модули можно найти в общей части). Если вы защитите свой диплом до окончания модулей, это позволит вам быть принятым на работу во время обучения.



В случае возникновения каких-либо блокировок с выполнением задания Вы можете обратиться к Своему Менеджеру ресурсов или авторам задания: Александру Толкачеву

