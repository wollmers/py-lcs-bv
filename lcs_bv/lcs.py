# from https://github.com/man1/Python-LCS/blob/master/lcs.py

### solve the longest common subsequence problem
"""
sub LLCS {
  my ($self,$X,$Y) = @_;

  my $m = scalar @$X;
  my $n = scalar @$Y;

  my $c = [];

  for my $i (0..1) {
    for my $j (0..$n) {
      $c->[$i][$j]=0;
    }
  }

  my ($i,$j);

  for ($i=1; $i <= $m; $i++) {
    for ($j=1; $j <= $n; $j++) {
      if ($X->[$i-1] eq $Y->[$j-1]) {
        $c->[1][$j] = $c->[0][$j-1]+1;
      }
      else {
        $c->[1][$j] = max($c->[1][$j-1],$c->[0][$j]);
      }
    }
    for ($j = 1; $j <= $n; $j++) {
      $c->[0][$j] = $c->[1][$j];
    }
  }
  return ($c->[1][$n]);
}
"""

# get the matrix of LCS lengths at each sub-step of the recursive process
# (m+1 by n+1, where m=len(list1) & n=len(list2) ... it's one larger in each direction
# so we don't have to special-case the x-1 cases at the first elements of the iteration
def lcs_mat(list1, list2):
	m = len(list1)
	n = len(list2)
	# construct the matrix, of all zeroes
	mat = [[0] * (n+1) for row in range(m+1)]
	# populate the matrix, iteratively
	for row in range(1, m+1):
		for col in range(1, n+1):
			if list1[row - 1] == list2[col - 1]:
				# if it's the same element, it's one longer than the LCS of the truncated lists
				mat[row][col] = mat[row - 1][col - 1] + 1
			else:
				# they're not the same, so it's the the maximum of the lengths
				# of the LCSs of the two options (different list truncated in each case)
				mat[row][col] = max(mat[row][col - 1], mat[row - 1][col])
	# the matrix is complete
	return mat

# backtracks all the LCSs through a provided matrix
def all_lcs(lcs_dict, mat, list1, list2, index1, index2):
	# if we've calculated it already, just return that
	# https://stackoverflow.com/questions/33727149/dict-object-has-no-attribute-has-key
	if (lcs_dict.__contains__((index1, index2))): return lcs_dict[(index1, index2)]
	# otherwise, calculate it recursively
	if (index1 == 0) or (index2 == 0): # base case
		return [[]]
	elif list1[index1 - 1] == list2[index2 - 1]:
		# elements are equal! Add it to all LCSs that pass through these indices
		lcs_dict[(index1, index2)] = [prevs + [list1[index1 - 1]] for prevs in all_lcs(lcs_dict, mat, list1, list2, index1 - 1, index2 - 1)]
		return lcs_dict[(index1, index2)]
	else:
		lcs_list = [] # set of sets of LCSs from here
		# not the same, so follow longer path recursively
		if mat[index1][index2 - 1] >= mat[index1 - 1][index2]:
			before = all_lcs(lcs_dict, mat, list1, list2, index1, index2 - 1)
			for series in before: # iterate through all those before
				if not series in lcs_list: lcs_list.append(series) # and if it's not already been found, append to lcs_list
		if mat[index1 - 1][index2] >= mat[index1][index2 - 1]:
			before = all_lcs(lcs_dict, mat, list1, list2, index1 - 1, index2)
			for series in before:
				if not series in lcs_list: lcs_list.append(series)
		lcs_dict[(index1, index2)] = lcs_list
		return lcs_list

# return a set of the sets of longest common subsequences in list1 and list2
def lcs(list1, list2):
	# mapping of indices to list of LCSs, so we can cut down recursive calls enormously
	mapping = dict()
	# start the process...
	return all_lcs(mapping, lcs_mat(list1, list2), list1, list2, len(list1), len(list2));

# return the length of LCS
def llcs(list1,list2):
    mat = lcs_mat(list1, list2)
    return mat[-1][-1]

### main ###

def main():
    # get two lists
	f = open("lists.txt")
	contents = f.read().split("\t")
	# l1 = [str(i) for i in contents[0].split(",")]
	print(contents[0])
	l1 = list(contents[0])
	print(l1)
	# l2 = [str(i) for i in contents[1].split(",")]
	print(contents[1])
	l2 = list(contents[1])
	print(l2)
	expect = int(contents[2])
	lists = lcs(l1, l2)
	for l in lists:
		print(l)

	print(llcs(l1, l2))

if __name__ == "__main__":
    main()
