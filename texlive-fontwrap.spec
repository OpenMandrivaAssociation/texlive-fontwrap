Name:		texlive-fontwrap
Version:	15878
Release:	1
Summary:	Bind fonts to specific unicode blocks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/xetex/latex/fontwrap
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fontwrap.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fontwrap.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package (which runs under XeLaTeX) lets you bind fonts to
specific unicode blocks, for automatic font tagging of
multilingual text. The package uses Perl (via perltex) to
construct its tables.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/xelatex/fontwrap
%doc %{_texmfdistdir}/doc/xelatex/fontwrap

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
