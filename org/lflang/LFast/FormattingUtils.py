#!/usr/bin/env python
""" generated source for module FormattingUtils """
# package: org.lflang.LFast
# 
#  * Utility functions that determine the specific behavior of the LF formatter.
#  * @author {Peter Donovan <peterdonovan@berkeley.edu>}
#  * @author {Billy Bao <billybao@berkeley.edu>}
#  
import re


class FormattingUtils(object):
    """ generated source for class FormattingUtils """
    # The minimum number of columns that should be allotted to a comment.
    # This is relevant in case of high indentation/small wrapLength.
    #       
    MINIMUM_COMMENT_WIDTH_IN_COLUMNS = 15

    #  Match a multiline comment. 
    MULTILINE_COMMENT = re.compile("\\s*/\\*\\v?(\\V*\\v+)*\\V*")

    #  The number of spaces to prepend to a line per indentation level. 
    INDENTATION = 4
    DEFAULT_LINE_LENGTH = 80
    MAX_WHITESPACE_USED_FOR_ALIGNMENT = 20
    BADNESS_PER_CHARACTER_VIOLATING_LINE_LENGTH = 20
    BADNESS_PER_LEVEL_OF_COMMENT_DISPLACEMENT = 1000
    BADNESS_PER_NEWLINE = 1

    # Return a String representation of {@code object}, with lines wrapped at
    # {@code lineLength}.
    #
    def render(self, object, lineLength):
        pass
    #       public static String render(EObject object, int lineLength) {
    #           MalleableString ms = ToLf.instance.doSwitch(object);
    #            singleLineCommentPrefix = getSingleLineCommentPrefix(object);
    #            ms.findBestRepresentation(
    #                 ms.render(INDENTATION, singleLineCommentPrefix),
    #                 r.levelsOfCommentDisplacement() * BADNESS_PER_LEVEL_OF_COMMENT_DISPLACEMENT
    #                    + countCharactersViolatingLineLength(lineLength).applyAsLong(r.rendering())
    #                        * BADNESS_PER_CHARACTER_VIOLATING_LINE_LENGTH
    #                    + countNewlines(r.rendering()) * BADNESS_PER_NEWLINE,
    #                lineLength,
    #                INDENTATION,
    #                singleLineCommentPrefix
    #            );
    #            var optimizedRendering = ms.render(INDENTATION, singleLineCommentPrefix);
    #            List comments = optimizedRendering.unplacedComments().toList();
    #            String r = "";
    #            if comments.stream().allMatch(String::isBlank) {
    #              r =  ? optimizedRendering.rendering();
    #            } else {
    #              r = lineWrapComments(comments, lineLength, singleLineCommentPrefix)
    #                    + "\n" + optimizedRendering.rendering();
    #            }
    #            return r
    #       }
    #      /**
    # Return the prefix that the formatter should use to mark the start of a
    # single-line comment.
    #
    def getSingleLineCommentPrefix(self, object):
        pass
    #      private static String getSingleLineCommentPrefix(EObject object) {
    #          if (object instanceof Model model) {
    #              var targetDecl = ASTUtils.targetDecl(model);
    #              if (targetDecl != null && targetDecl.__name__.toUpperCase().contains("PYTHON")) {
    #                  return "#";
    #              }
    #          }
    #          return "//";

    #
    #      /**
    # Return a String representation of {@code object} using a reasonable
    # default line length.
    #
    #      public static String render(EObject object) { return render(object, DEFAULT_LINE_LENGTH); }
    #

#      /**
# Return the number of characters appearing in columns exceeding {@code lineLength}.
#
    def countCharactersViolatingLineLength(self, lineLength):
        pass
#      private static ToLongFunction countCharactersViolatingLineLength(int lineLength) {
#          return s -> s.lines().mapToInt(it -> max(0, it.length() - lineLength)).sum();
#      }
#
    def countNewlines(self, s):
        pass
#      private static long countNewlines(String s) {
#          return s.lines().count();
#      }
# 
#      /**
# Break lines at spaces so that each line is no more than {@code width}
# columns long, if possible. Normalize whitespace. Merge consecutive
# single-line comments.
#
    def lineWrapComments(self, comments, width, singleLineCommentPrefix):
        pass
#      static String lineWrapComments(
#          List comments,
#          int width,
#          String singleLineCommentPrefix
#      ) {
#          StringBuilder ret = new "";
#          StringBuilder current = new "";
#          for (String comment : comments) {
#              if (comment.stripLeading().startsWith("/*")) {
#                  if (!ret.isEmpty() && !current.isEmpty()) ret.append("\n");
#                  ret.append(lineWrapComment(current.__str__(), width, singleLineCommentPrefix));
#                  current.setLength(0);
#                  if (!ret.isEmpty()) ret.append("\n");
#                  ret.append(lineWrapComment(comment.strip(), width, singleLineCommentPrefix));
#              } else {
#                  if (!current.isEmpty()) current.append("\n");
#                  current.append(comment.strip());
#              }
#          }
#          if (!ret.isEmpty() && !current.isEmpty()) ret.append("\n");
#          ret.append(lineWrapComment(current.__str__(), width, singleLineCommentPrefix));
#          return ret.__str__();
#      }
#      /** Wrap lines. Do not merge lines that start with weird characters. 
#      private static String lineWrapComment(
#          String comment,
#          int width,
#          String singleLineCommentPrefix
#      ) {
#          width = max(width, MINIMUM_COMMENT_WIDTH_IN_COLUMNS);
#          List paragraphs = Arrays.stream(
#              comment.strip()
#                  .replaceAll("^/?((\\*|//|#)\\s*)+", "")
#                  .replaceAll("\\s*\\*/$", "")
#                  .replaceAll("(?<=(\\r\\n|\\r|\\n))\\h*(\\*|//|#)\\h*", "")
#                  .split("(\n\\s*){2,}")
#              ).map(s -> Arrays.stream(s.split("(\\r\\n|\\r|\\n)\\h*(?=[@#$%^&*\\-+=:;<>/])")))
#              .map(stream -> stream.map(s -> s.replaceAll("\\s+", " ")))
#              .map(Stream::toList)
#              .toList();
#          if (MULTILINE_COMMENT.matcher(comment).matches()) {
#              if (len(paragraphs) == 1 && paragraphs.get(0).size() == 1) {
#                  String singleLineRepresentation = String.format(
#                      "/** %s */", paragraphs.get(0).get(0)
#                  );
#                  if (singleLineRepresentation.length() <= width) return singleLineRepresentation;
#              }
#              return String.format("/**\n%s\n */", lineWrapComment(paragraphs, width, " * "));
#          }
#          return lineWrapComment(paragraphs, width, singleLineCommentPrefix + " ");
#      }
# 
#      /**
# Wrap lines.
# @param paragraphs A list of lists of subparagraphs.
# @param width The preferred maximum number of columns per line.
# @param linePrefix A string to prepend to each line of comment.
#       
#      private static String lineWrapComment(
#          List paragraphs,
#          int width,
#          String linePrefix
#      ) {
#          int widthAfterPrefix = max(
#              width - linePrefix.length(),
#              MINIMUM_COMMENT_WIDTH_IN_COLUMNS
#          );
#          return paragraphs.stream()
#              .map(paragraph -> wrapLines(paragraph, widthAfterPrefix)
#                  .map(s -> (linePrefix + s.stripLeading()).stripTrailing())
#                  .collect(Collectors.joining("\n"))
#              ).collect(Collectors.joining(String.format("\n%s\n", linePrefix.stripTrailing())));
#      }
# 
#      /** Wrap a given paragraph.
    def wrapLines(self, subparagraphs, width):
        pass
#      private static Stream wrapLines(List subparagraphs, int width) {
#          var ret = new [];
#          for (String s : subparagraphs) {
#              int numCharactersProcessed = 0;
#              while (numCharactersProcessed + width < s.length()) {
#                  // try to wrap at space
#                  int breakAt = s.lastIndexOf(' ', numCharactersProcessed + width);
#                  // if unable to find space in limit, extend to the first space we find
#                  if (breakAt < numCharactersProcessed) {
#                      breakAt = s.indexOf(' ', numCharactersProcessed + width);
#                  }
#                  if (breakAt < numCharactersProcessed) breakAt = s.length();
#                  ret.append(s.substring(numCharactersProcessed, breakAt));
#                  numCharactersProcessed = breakAt + 1;
#              }
#              if (numCharactersProcessed < s.length()) ret.append(s.substring(numCharactersProcessed));
#          }
#          return ret.stream();
#      }
# 
#      /**
# Merge {@code comment} into the given list of strings without changing the
# length of the list, preferably in a place that indicates that
# {@code comment} is associated with the {@code i}th string.
# @param comment A comment associated with an element of
# {@code components}.
# @param components A list of strings that will be rendered in sequence.
# @param i The position of the component associated with {@code comment}.
# @param width The ideal number of columns available for comments that
# appear on their own line.
# @param keepCommentsOnSameLine Whether to make a best-effort attempt to
# keep the comment on the same line as the associated string.
# @param singleLineCommentPrefix The prefix that marks the start of a
# single-line comment.
# @param startColumn The ideal starting column of a comment
# @return Whether the comment placement succeeded.
#
    def placeComment(self, comment, components, i, width, keepCommentsOnSameLine, singleLineCommentPrefix, startColumn):
        pass
#      static boolean placeComment(
#          List comment,
#          List components,
#          int i,
#          int width,
#          boolean keepCommentsOnSameLine,
#          String singleLineCommentPrefix,
#          int startColumn
#      ) {
#          if (comment.stream().allMatch(String::isBlank)) return true;
#          String wrapped = FormattingUtils.lineWrapComments(comment, width, singleLineCommentPrefix);
#          if (keepCommentsOnSameLine && wrapped.lines().count() == 1 && !wrapped.startsWith("/**")) {
#              int cumsum = 0;
#              for (int j = 0; j < len(components); j++) {
#                  String current = components.get(j);
#                  if (j >= i && current.contains("\n")) {
#                      components.set(j, components.get(j).replaceFirst(
#                          "\n",
#                          " ".repeat(max(
#                              2,
#                              startColumn - cumsum - components.get(j).indexOf("\n")
#                          )) + wrapped + "\n"
#                      ));
#                      return true;
#                  } else if (current.contains("\n")) {
#                      cumsum = current.length() - current.lastIndexOf("\n") - 1;
#                  } else {
#                      cumsum += current.length();
#                  }
#              }
#          }
#          for (int j = i - 1; j >= 0; j--) {
#              if (components.get(j).endsWith("\n")) {
#                  components.set(j, String.format("%s%s\n", components.get(j), wrapped));
#                  return true;
#              }
#          }
#          return false;
#      }
#  }
