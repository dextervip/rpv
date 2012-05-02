-- phpMyAdmin SQL Dump
-- version 3.4.5
-- http://www.phpmyadmin.net
--
-- Servidor: localhost
-- Tempo de Geração: 02/05/2012 às 22h28min
-- Versão do Servidor: 5.5.16
-- Versão do PHP: 5.3.8

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Banco de Dados: `gerendisp_db`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `disciplinas_newdisciplina`
--

CREATE TABLE IF NOT EXISTS `disciplinas_newdisciplina` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(150) NOT NULL,
  `codigo` varchar(50) NOT NULL,
  `curso` varchar(150) NOT NULL,
  `campus` varchar(150) NOT NULL,
  `cargaHora` varchar(5) NOT NULL,
  `creditosPraticos` varchar(20) NOT NULL,
  `creditosTeoricos` varchar(20) NOT NULL,
  `anoLetivo` varchar(10) NOT NULL,
  `turno` varchar(20) NOT NULL,
  `turma` varchar(20) NOT NULL,
  `ementa` longtext NOT NULL,
  `ojetivos` longtext NOT NULL,
  `preRequisitos` longtext NOT NULL,
  `bibliograBasica` longtext NOT NULL,
  `bibliograComplem` longtext NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nome` (`nome`),
  UNIQUE KEY `codigo` (`codigo`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=13 ;

--
-- Extraindo dados da tabela `disciplinas_newdisciplina`
--

INSERT INTO `disciplinas_newdisciplina` (`id`, `nome`, `codigo`, `curso`, `campus`, `cargaHora`, `creditosPraticos`, `creditosTeoricos`, `anoLetivo`, `turno`, `turma`, `ementa`, `ojetivos`, `preRequisitos`, `bibliograBasica`, `bibliograComplem`) VALUES
(2, 'Resolução de Problemas V', 'AL0233', 'Engenharia de Software', 'Alegrete', '120h', '6', '2', '2012/01', 'Noite', '10', 'Diferenciação entre métodos tradicionais e ágeis. Instanciação de processo de acordo com objetivos do projeto.\r\nExecução de processo de desenvolvimento de software.', 'Objetivo Geral:\r\nProver aos alunos uma experimentação em termos de metodologias de desenvolvimento de software que\r\ngarantam uma plena cobertura de práticas de engenharia de software orientadas à qualidade e produtividade.\r\nObjetivos Específicos:\r\n• Identificar a aplicabilidade de uma metodologia a um projeto de software.\r\n• Executar uma metodologia em projeto de desenvolvimento de software.\r\n• Gerar evidências claras e objetivas da execução de uma metodologia.', 'Não', 'HELDMAN, Kim. Gerência de projetos: guia para o exame oficial do PMI. 5. ed. Rio de Janeiro: Elsevier,\r\n2009.\r\nPRESSMAN, Roger S. Engenharia de Software. 6. ed. São Paulo: McGraw-Hill, 2006.\r\nSOMMERVILLE, Ian. Engenharia de software. 8. ed. São Paulo: Pearson Prentice Hall, 2007.', 'SALLES JR., Carlos A. C.; et al. Gerenciamento de riscos em projetos. 2. ed. Rio de Janeiro: FGV, 2010.\r\nMOLINARI, Leonardo. Gerencia de configuração: técnicas e praticas no desenvolvimento do software.\r\nFlorianópolis: Visual Books, 2007.\r\nNORMAN, Eric S. Estruturas analíticas de projeto: a base para a excelência em gerenciamento de projetos. São\r\nPaulo: Blucher, 2008.\r\nPFLEEGER, Shari L. Engenharia de software: teoria e pratica. 2.ed. São Paulo: Prentice Hall, 2004.\r\nVIEIRA, Marconi F. Gerenciamento de projetos de tecnologia da informação 2. ed. Rio de Janeiro: Elsevier,\r\n2007.'),
(3, 'Redes e Sistemas Distribuídos', 'AL0231', 'Engenharia de Software', 'Alegrete', '60', '2', '2', '2012/01', 'Noite', '10', 'Introdução a redes de computadores. Tipos e topologias de redes. Modelos de referência ISO/OSI e TCP/IP.\r\nEstudo das Camadas que compõem os modelos de referência com ênfase na camada de aplicação.\r\nIntrodução a sistemas distribuídos. Modelos de arquitetura e modelos fundamentais. Comunicação entre\r\nprocessos. Sincronização em sistemas distribuídos. Objetos distribuídos e invocação remota. Estudo de caso\r\nusando RMI Java e CORBA.', 'Objetivo Geral:\r\nEsta disciplina visa descrever os conceitos básicos relacionados a redes de computadores e sistemas\r\ndistribuídos.\r\nObjetivos Específicos:\r\n• Compreender os conceitos e características de redes de computadores;\r\n• Analisar, projetar, implementar e avaliar sistemas de processamento de informação que utilizem\r\ntransmissão de dados;\r\n• Compreender os conceitos, características e ferramentas existentes nos sistemas distribuídos;\r\n• Identificar os componentes de um sistema distribuído;\r\n• Identificar técnicas para comunicação entre processos;\r\n• Implementar sistemas distribuídos;', 'Nenhum', 'Tanenbaum, A. S. “Sistemas Distribuídos: Princípios e Paradigmas”. 2a ed., Pearson Prentice Hall, 2008.\r\nTanenbaum, A. S. “Redes de Computadores”. Rio de Janeiro, Campus, 2003.\r\nCoulouris, G. “Sistemas Distribuídos: Conceitos e Projeto”. 4a ed., Addison Wesley, 2005.\r\nReferências Complementares', 'Kurose, J. F.; Ross, K. W. “Redes de Computadores e a Internet: uma abordagem top-down”. Pearson\r\nAddison Wesley, 2006.\r\nComer, D. E. “Interligação de Redes com TCP/IP”. Campus, 2006.\r\nDollimore, J.; Kindberg, T.; Coulouris, G. “Distributed Systems: concepts and design”. 4a ed., Addison\r\nWesley, 2005.\r\nTel, G. “Introduction to Distributed Algorithms”. 2a ed., Cambridge University Press, 2001.\r\nLynch, N. A. “Distributed Algorithms”. Morgan Kaufmann, 1997.\r\nStevens, W. R.; Fenner, B.; Rudoff, A. M. “Unix Network Programming Volume 1: the sockets networking\r\nAPI”. Addison-Wesley Professional, 2003.\r\nStevens, W. R. “TCP/IP Illustrated Volume 1: the protocols”. Addison-Wesley Professional, 1994.\r\nStevens, W. R. “TCP/IP Illustrated Volume 3: TCP for transactions, HTTP, NNTP, and the UNIX domain\r\nprotocols”. Addison-Wesley Professional, 1996.'),
(4, 'Qualidade de Software', 'Não Tem', 'Engenharia de Software', 'Alegrete', '30', '0', '2', '2012/01', 'Noite', '10', 'Histórico e conceitos sobre qualidade. Qualidade de processo e produto de software. Normas de qualidade de\r\nsoftware.', 'Geral:\r\nAplicar de forma sistêmica os princípios da gerência da qualidade no processo de desenvolvimento de software a fim\r\nde obter qualidade no produto.\r\nEspecífico:\r\n• Indicar os elementos necessários para garantir a qualidade no processo de desenvolvimento de um software;\r\n• Identificar os principais modelos de gestão da qualidade de software;\r\n• Identificar características de qualidade do produto de software.', 'Nenhum', 'KOSCIANSKI, André; SOARES, Michel dos S.: Qualidade de Software. 2a. edição. Editora Novatec. 2007.\r\nISBN: 978-85-7522-112-9.\r\n• SILVA, Ivan J. M.; OLIVEIRA, Vivianne: Qualidade em Software. Editora Alta Books. 2005. ISBN:\r\n8576080737.\r\n• CAMPOS, Vicente F.: TQC: Controle de Qualidade Total (no estilo japonês). Editora INDG, 8a. edição,\r\n2004.', 'MALDONADO, José C.; DELAMARO, Márcio E.; JINO, Mario: Introdução ao Teste de Software. Ed.\r\nCampus. 2007. ISBN-10: 85-352-2634-6. ISBN-13: 978-85-352-2634-8\r\n• BARTIÉ, Alexandre: Garantia da Qualidade de Software: Adquirindo Maturidade Organizacional. Ed.\r\nCampus. ISBN: 8535211241\r\n• PFLEEGER, Shari L.: Engenharia de Software - Teoria e Prática. 2a ed., São Paulo, Prentice Hall, 2004.\r\n• PRESSMAN, Roger S.. Engenharia de Software. 6a ed., São Paulo, McGraw-Hill, 2006.\r\n• SOMMERVILLE, Ian. Engenharia de Software. 8a ed., São Paulo, Addison-Wesley, 2007.'),
(5, 'Processo de Doftware', 'AL0229', 'Engenharia de Software', 'Alegrete', '30', '0', '2', '2012/01', 'Noite', '10', 'Introdução ao processo de software. Análise dos modelos prescritivos de processo. Gerenciamento de processo\r\nde software.', 'Objetivo Geral:\r\nAo final da disciplina o aluno deve conhecer os principais conceitos relacionados ao processo de software,\r\ntornando-se apto a aplicar um processo em um projeto de software.\r\nObjetivos Específicos:\r\n• Conhecer as principais alternativas de processo de software existentes.\r\n• Saber instanciar um processo de acordo com as necessidades do projeto de software.', 'Nenhum', 'SOMMERVILLE, Ian. Engenharia de Software. 8. ed., São Paulo, Pearson Addison-Wesley, 2007.\r\nPRESSMAN, Roger S.. Engenharia de Software. 6. ed., São Paulo, McGraw-Hill, 2006.\r\nFILHO, Wilson de Pádua P.. Engenharia de Software: Fundamentos, Métodos e Padrões. 3. ed., Rio de\r\nJaneiro, LTC, 2009.', 'KRUCHTEN, P. Introdução ao RUP - Rational Unified Process. 2. ed., Rio de Janeiro, Editora Ciência\r\nModerna Ltda., 2003.\r\nJÚNIOR, H. E., Engenharia de Software na Prática. São Paulo, Novatec, 2010.\r\nPFLEEGER, S. L., Engenharia de software :teoria e prática. 2.ed. Sao Paulo, Prentice Hall, 2004.\r\nTONSIG, S. L., Engenharia de software :analise e projeto de sistemas. 2. ed. Rio de Janeiro, Ciência\r\nModerna, c2008\r\nSCHACH, S. R., Engenharia de software : os paradigmas clássicos e orientado a objetos. 7. ed. Sao Paulo,\r\nMc Graw Hill, 2009.'),
(6, 'Práticas de desenvolvimento de Software', 'AL2064', 'Ciência da Computação/Eng. de Software', 'Alegrete', '60', '3', '1', '2012/01', 'Noite', '10', 'Introdução a ferramentas de desenvolvimento de software, como\r\ngerenciadores de versão de código, rastreadores de falhas, automação de\r\ncompilação, gerenciadores de casos de teste, Ambientes de\r\nDesenvolviemento Integrado (IDE), etc, e exemplos de suas aplicações em\r\nprojetos consolidados de software livre.', 'Objetivo Geral:\r\nApresentar conceitos e ferramentas utilizadas no desenvolvimento de\r\nsoftware e sua aplicação/utilização em projetos de software livre. A escolha\r\nde tal aplicação permite que os alunos possam, se desejarem, interagir com\r\nas comunidades de software livre sobre o uso de tais ferramentas e métodos.\r\nObjetivos Específicos:\r\n• Permitir ao aluno ver na prática a aplicação dos conceitos vistos no\r\ndecorrer do curso.\r\n• Aproximar os alunos de comunidades ativas de desenvolvimento de\r\nsoftware, ampliando sua rede de contatos.\r\n• Familiarizar o aluno com o conjunto de ferramentas a seu dispor para o\r\ndesenvolvimento de softwares.', 'Não há', 'Engenharia de Software - Pressman\r\nCode Complete: A Practical Handbook of Software Construction - Steve\r\nMcConnell\r\nPadrões de projeto - Erich Gamma\r\nOpen Advice – Lidya Pintscher et al. Disponível em www.open-advice.org', 'Definitive Guide to GCC - William Von Hagen\r\nIntrodução ao teste de Software - José Carlos Maldonado\r\nImplementando o desenvolvimento lean de software - Poppendieck, Mary /\r\nPoppendieck, Tom\r\nFoundations of GTK+ Development - Andrew Krause\r\nParadigmas do software Aberto - Tercio Pacitti'),
(7, 'INTRODUÇÃO A SISTEMAS DE COMPUTAÇÃO', 'AL0220', 'ENGENHARIA DE SOFTWARE', 'Alegrete', '60', '0', '4', '2011/02', 'Noite', '10', 'Noções de Organização e Arquitetura de Computadores, e Sistemas Operacionais. Processos de\r\nCompilação e Montagem. Otimização de desempenho via Pipeline e Arquiteturas Superescalares.', 'Apresentar os princípios básicos da arquitetura e organização de sistemas de computação, bem\r\ncomo introduzir conceitos básicos de Sistemas Operacionais. Tais conhecimentos devem auxiliar o\r\naluno a desenvolver melhores práticas de programação já que o mesmo estará apto a\r\ncompreender como o software por ele desenvolvido será tratado internamente pelo sistema.', 'Nenhum', 'PATTERSON, D.A.; HENNESSY, J.L.. Organização e Projeto de Computadores. Rio de Janeiro, RJ,\r\nElsevier, 2005.\r\nSILBERSCHATZ, A.; GALVIN, P.B.; GAGNE, G.. Sistemas Operacionais com Java. 7a Ed. Elsevier. Rio de\r\nJaneiro, 2008.\r\nTANENBAUM, A.S.', 'STALLINGS, W.. Arquitetura e Organização de Computadores: Projeto para o desempenho. 5a Ed.\r\nPrentice Hall. São Paulo, SP, 2002.\r\nMURDOCCA, M.J.. Introdução à Arquitetura de Computadores. Rio de Janeiro, Campus, 2001.\r\nHENNESSY, J.L.. Arquitetura de Computadores: uma abordagem quantitativa. Rio de Janeiro, Campus,\r\n2003.\r\nTANENBAUM, A.S.. Sistemas Operacionais Modernos. 3a ed., Pearson PrenticeHall, 2009.\r\nOLIVEIRA, R.S.; CARISSIMI, A.S.; TOSCANI, SIMÃO S.. Sistemas Operacionais. 4a ed., Porto Alegre,\r\nBookman, 2010.');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
