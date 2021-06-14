create table if not exists genre(
	id serial primary key,
	name varchar(40) not null
);

create table if not exists singer(
	id serial primary key,
	name varchar(40) not null
);

create table if not exists album(
	id serial primary key,
	name varchar(40) not null,
	year integer not null
);

create table if not exists track(
	id serial primary key,
	name varchar(40) not null,
	album_id integer not null references album(id),
	duration numeric(3,2) 
);

create table if not exists collection(
	id serial primary key,
	name varchar(40) not null,
	year integer not null
);

create table if not exists singer_genre(
	id serial primary key,
	singer_id integer not null references singer(id),
	genre_id integer not null references genre(id)
);

create table if not exists singer_album(
	id serial primary key,
	singer_id integer not null references singer(id),
	album_id integer not null references album(id)
);

create table if not exists track_collection(
	id serial primary key,
	track_id integer references track(id),
	collection_id integer not null references collection(id)
);
