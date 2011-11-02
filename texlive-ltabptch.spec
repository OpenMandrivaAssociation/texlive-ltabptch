Name:		texlive-ltabptch
Version:	1.74d
Release:	1
Summary:	Bug fix for longtable
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ltabptch
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ltabptch.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ltabptch.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
A patch for LaTeX bugs tools/3180 and tools/3480. The patch
applies to version 4.11 of longtable.

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
%{_texmfdistdir}/tex/latex/ltabptch/ltabptch.sty
%doc %{_texmfdistdir}/doc/latex/ltabptch/README
%doc %{_texmfdistdir}/doc/latex/ltabptch/ltabptch.pdf
%doc %{_texmfdistdir}/doc/latex/ltabptch/ltabptch.tex
%doc %{_texmfdistdir}/doc/latex/ltabptch/ltabtest.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}