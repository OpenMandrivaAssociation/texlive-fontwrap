# revision 15878
# category Package
# catalog-ctan /macros/xetex/latex/fontwrap
# catalog-date 2008-08-19 20:38:14 +0200
# catalog-license gpl
# catalog-version undef
Name:		texlive-fontwrap
Version:	20080819
Release:	1
Summary:	Bind fonts to specific unicode blocks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/xetex/latex/fontwrap
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fontwrap.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fontwrap.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package (which runs under XeLaTeX) lets you bind fonts to
specific unicode blocks, for automatic font tagging of
multilingual text. The package uses Perl (via perltex) to
construct its tables.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/xelatex/fontwrap/fontwrap.sty
%doc %{_texmfdistdir}/doc/xelatex/fontwrap/README
%doc %{_texmfdistdir}/doc/xelatex/fontwrap/fontwrap.pdf
%doc %{_texmfdistdir}/doc/xelatex/fontwrap/fontwrap.tex
%doc %{_texmfdistdir}/doc/xelatex/fontwrap/fontwrap_example.pdf
%doc %{_texmfdistdir}/doc/xelatex/fontwrap/fontwrap_example.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
