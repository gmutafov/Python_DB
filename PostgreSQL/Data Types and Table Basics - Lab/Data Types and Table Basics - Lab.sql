PGDMP      0                |           gamebar    16.3    16.3     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    16450    gamebar    DATABASE     �   CREATE DATABASE gamebar WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_United States.1252';
    DROP DATABASE gamebar;
                postgres    false            �            1259    16452 	   employees    TABLE     1  CREATE TABLE public.employees (
    id integer NOT NULL,
    first_name character varying(30),
    last_name character varying(50),
    hiring_date date DEFAULT '2023-01-01'::date NOT NULL,
    salary numeric(10,2) DEFAULT 0 NOT NULL,
    devices_number integer,
    middle_name character varying(100)
);
    DROP TABLE public.employees;
       public         heap    postgres    false            �            1259    16451    employees_id_seq    SEQUENCE     �   CREATE SEQUENCE public.employees_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.employees_id_seq;
       public          postgres    false    216            �           0    0    employees_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.employees_id_seq OWNED BY public.employees.id;
          public          postgres    false    215            �            1259    16469    issues    TABLE     �   CREATE TABLE public.issues (
    id integer NOT NULL,
    description character varying(150),
    date date,
    start timestamp without time zone
);
    DROP TABLE public.issues;
       public         heap    postgres    false            �            1259    16468    issues_id_seq    SEQUENCE     �   CREATE SEQUENCE public.issues_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 $   DROP SEQUENCE public.issues_id_seq;
       public          postgres    false    218            �           0    0    issues_id_seq    SEQUENCE OWNED BY     ?   ALTER SEQUENCE public.issues_id_seq OWNED BY public.issues.id;
          public          postgres    false    217                       2604    16455    employees id    DEFAULT     l   ALTER TABLE ONLY public.employees ALTER COLUMN id SET DEFAULT nextval('public.employees_id_seq'::regclass);
 ;   ALTER TABLE public.employees ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    216    215    216            "           2604    16472 	   issues id    DEFAULT     f   ALTER TABLE ONLY public.issues ALTER COLUMN id SET DEFAULT nextval('public.issues_id_seq'::regclass);
 8   ALTER TABLE public.issues ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    218    217    218            �          0    16452 	   employees 
   TABLE DATA           p   COPY public.employees (id, first_name, last_name, hiring_date, salary, devices_number, middle_name) FROM stdin;
    public          postgres    false    216   �       �          0    16469    issues 
   TABLE DATA           >   COPY public.issues (id, description, date, start) FROM stdin;
    public          postgres    false    218          �           0    0    employees_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.employees_id_seq', 3, true);
          public          postgres    false    215            �           0    0    issues_id_seq    SEQUENCE SET     <   SELECT pg_catalog.setval('public.issues_id_seq', 1, false);
          public          postgres    false    217            $           2606    16458    employees employees_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.employees
    ADD CONSTRAINT employees_pkey PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.employees DROP CONSTRAINT employees_pkey;
       public            postgres    false    216            &           2606    16474    issues issues_pkey 
   CONSTRAINT     P   ALTER TABLE ONLY public.issues
    ADD CONSTRAINT issues_pkey PRIMARY KEY (id);
 <   ALTER TABLE ONLY public.issues DROP CONSTRAINT issues_pkey;
       public            postgres    false    218            �   Q   x�3������te�F�F�@d�ihb`�gb�ihd���e�鋢�D��������̘�E��4S�2��=... �!K      �      x������ � �     