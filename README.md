<div align="center">
  <h1 style="font-size: 32px; border: none; line-height: 0; font-weight: bold">🛒 Ecommerce API</h1>
  <p>API REST desenvolvida com Django e Django REST Framework para sistema de e-commerce completo</p>
    <div style="margin-bottom: 10px">
    <img src="https://img.shields.io/badge/Language-Python-blue.svg" alt="Language: Python"/>
    <img src="https://img.shields.io/badge/Framework-Django-green.svg" alt="Framework: Django"/>
    <img src="https://img.shields.io/badge/API-DRF-orange.svg" alt="API: Django REST Framework"/>
    <img src="https://img.shields.io/badge/Database-PostgreSQL-blue.svg" alt="Database: PostgreSQL"/>
    <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License: MIT"/>
    </div>
    <br>
</div>

# Links Rápidos

- [Descrição](#descrição)
- [Arquitetura do Sistema](#arquitetura-do-sistema)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Configuração](#configuração)
- [Uso](#uso)
- [Testes](#testes)
- [Funcionalidades](#funcionalidades)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Contribuição](#contribuição)
- [Licença](#licença)

## Descrição

Esta API REST oferece um backend completo para sistemas de e-commerce, desenvolvida com **Django** e **Django REST Framework (DRF)**. A API fornece endpoints para gerenciamento de produtos, usuários, pedidos, carrinho de compras e autenticação.

### Características Principais

- 🔐 **Autenticação JWT** para segurança robusta
- 🛍️ **Gestão completa de produtos** com categorias e variações
- 🛒 **Sistema de carrinho** com persistência
- 📦 **Controle de pedidos** com rastreamento de status
- 👥 **Gerenciamento de usuários** com perfis personalizados
- 🔍 **Sistema de busca** e filtros avançados
- 📊 **Dashboard administrativo** integrado
- 🌐 **API RESTful** com documentação automática

## Arquitetura do Sistema

Este projeto faz parte de um ecossistema completo de e-commerce dividido em 3 repositórios:

- **[ecommerce-api](https://github.com/devGabrielNathan/ecommerce-api)** - Backend API (este repositório)
- **[ecommerce-client](https://github.com/devGabrielNathan/ecommerce-client)** - Frontend React
- **[ecommerce-compose](https://github.com/devGabrielNathan/ecommerce-compose)** - Orquestração Docker

## Pré-requisitos

Antes de começar, verifique se você possui as seguintes ferramentas instaladas:

- **Python** 3.12 ou superior
- **Poetry** (gerenciador de dependências)
- **PostgreSQL** (banco de dados)
- **Git** para controle de versão

## Instalação

### Passo 1: Clonar o repositório

```bash
git clone https://github.com/devGabrielNathan/ecommerce-api-drf.git
cd ecommerce-api-drf