


create table companies (
    id serial primary key,
    company_name varchar not null,
    company_director varchar not null,
    owner varchar not null,
    nation varchar,
    university varchar,
    company_code varchar
);