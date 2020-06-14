
Use AdventureWorks2017

--select query

Select * from Person.Password




-- select 2 highest ID in list  (Without Max in main query )

select top 1 BusinessEntityID from Person.Password where BusinessEntityID < (select Max (BusinessEntityID) from Person.Password) order by BusinessEntityID desc

-- select 2 highest ID in list  (With Max in main query )

select Max(BusinessEntityID) from Person.Password where BusinessEntityID < (select Max (BusinessEntityID) from Person.Password) 



select * from [Person].[Person]
-- Creating a table from existing data in another table
select BusinessEntityID INTO NewPerson from Person.Person where MiddleName = 'M'

select * INTO  NewPersonPassword from Person.Password where (BusinessEntityID%2) = 0

Select * from NewPerson

select * from Person.Person where BusinessEntityID IN (Select top 10 BusinessEntityID from NewPerson)

select * from [Person].[Password]

--inner Join Person.Person on NewPersonPassword

select P.PersonType,P.FirstName,P.LastName,P.rowguid,N.PasswordSalt,N.PasswordHash from Person.Person P Inner Join NewPersonPassword N ON P.BusinessEntityID = N.BusinessEntityID

select * from Person.Person P Outer Join NewPersonPassword N ON P.BusinessEntityID = N.BusinessEntityID



select * from  NewPersonPassword order by   ModifiedDate desc

