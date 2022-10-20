$latex = 'xelatex --no-pdf ' . $ENV{'LATEXOPTS'} . ' %O %S';
$pdflatex = 'xelatex ' . $ENV{'LATEXOPTS'} . ' %O %S';
$lualatex = 'lualatex ' . $ENV{'LATEXOPTS'} . ' %O %S';
$xelatex = 'xelatex --no-pdf ' . $ENV{'LATEXOPTS'} . ' %O %S';
$makeindex = 'internal xindy ' . $ENV{'XINDYOPTS'} . ' %O -o %D %S';
sub xindy {
  my @args = @_;
  if (-z $args[-1]) {
    # create an empty .ind file if .idx is empty
    open(FH, ">" . $args[-2]);
    close(FH);
    return 0;
  } else {
    return system("xindy", @args);
  }
}
add_cus_dep( "glo", "gls", 0, "makeglo" );
sub makeglo {
 return system( "makeindex -s gglo.ist -o '$_[0].gls' '$_[0].glo'" );
}