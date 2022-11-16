Name:		texlive-nchairx
Version:	60196
Release:	1
Summary:	Maths macros from chair X of Wurzburg University
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/nchairx
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nchairx.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nchairx.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nchairx.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package was developed by members of the chair for
mathematical physics at the University of Wurzburg as a
collection of macros and predefined environments for quickly
creating nice mathematical documents. (Note concerning the
package name: the "n" stands for "new", the "X" is a roman 10.)

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/nchairx
%{_texmfdistdir}/tex/latex/nchairx
%doc %{_texmfdistdir}/doc/latex/nchairx

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
