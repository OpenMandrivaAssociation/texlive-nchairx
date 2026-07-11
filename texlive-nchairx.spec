%global tl_name nchairx
%global tl_revision 60196

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0.0
Release:	%{tl_revision}.1
Summary:	Maths macros from chair X of Wurzburg University
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/nchairx
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/nchairx.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/nchairx.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/nchairx.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package was developed by members of the chair for mathematical
physics at the University of Wurzburg as a collection of macros and
predefined environments for quickly creating nice mathematical
documents. (Note concerning the package name: the "n" stands for "new",
the "X" is a roman 10.)

