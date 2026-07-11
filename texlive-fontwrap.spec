%global tl_name fontwrap
%global tl_revision 15878

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Bind fonts to specific unicode blocks
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/xetex/latex/fontwrap
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fontwrap.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fontwrap.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package (which runs under XeLaTeX) lets you bind fonts to specific
unicode blocks, for automatic font tagging of multilingual text. The
package uses Perl (via perltex) to construct its tables.

