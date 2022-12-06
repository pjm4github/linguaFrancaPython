
# Miscellaneous Java classes that need definition
from include.Multimap import LinkedHashMap
from include.overloading import overloaded
from lflang.lf.ActionOrigin import Collections

class AbstractElementFinder:
    pass

class AbstractGrammarElementFinder:
    pass

class AbstractParserRuleElementFinder:
    pass

class GrammarUtil:
    pass


class EcoreXtextSaveUpdateController:
    pass


class PInputEventListener:
    pass


class LflangActivator:
    pass


class LanguageSpecificURIEditorOpener:
    pass


class XtextEditor:
    pass

class XtextSelectionHighlighter:
    pass


def ElkPadding(param):
    return param


class LinkedHashSet:
    pass


class HashSet:
    pass


class CheckMode:
    pass


class CancelIndicator:
    pass


class LfIssue:
    pass


class ReportingBackend:
    pass


def Io():
    pass


class DefaultParser:
    pass


class Paths:
    pass


class Files:
    pass

class Util:
    pass


class Option:
    pass


class Options:
    def __init__(self):
        #  The serial version UID. */
        self.serialVersionUID = 1
        #
        #  a map of the options with the character key */
        self.shortOpts = LinkedHashMap()
        #
        #  a map of the options with the long key */
        self.longOpts = LinkedHashMap()
        #
        #  a map of the required options */
        #     // N.B. This can contain either a String (addOption) or an OptionGroup (addOptionGroup)
        #     // TODO this seems wrong
        self.requiredOpts = []
        #
        #  a map of the option groups */
        self.optionGroups = LinkedHashMap()

    def addOptionGroup(self, group):
        """
        Add the specified option group.

        @param group the OptionGroup that is to be added
        @return the resulting Options instance
        :param group:
        :return:
        """
        if group.isRequired():
            self.requiredOpts.append(group)
        for option in group.getOptions():
            # an Option cannot be required if it is in an
            # OptionGroup, either the group is required or
            # nothing is required
            option.setRequired(False)
            self.addOption(option)

            self.optionGroups.put(option.getKey(), group)
        return self


    def getOptionGroups(self):
        """
        Lists the OptionGroups that are members of this Options instance.
        @return a Collection of OptionGroup instances.
        :return:
        """
        return HashSet(self.optionGroups.values())

    @classmethod
    @overloaded
    def addOption(self, opt, description):
        """
        Add an option that only contains a short name.
        <p>
        The option does not take an argument.
        </p>
        @param opt Short single-character name of the option.
        @param description Self-documenting description
        @return the resulting Options instance
        @since 1.3
            public Options
        :param opt:
        :param description:
        :return:
        """
        self.addOption(opt, None, False, description)
        return self

    @addOption.register(object, str, bool, str)
    def addOption_0(self, opt, hasArg, description):
        """
        Add an option that only contains a short-name.
        <p>
        It may be specified as requiring an argument.
        </p>
        @param opt Short single-character name of the option.
        @param hasArg flag signally if an argument is required after this option
        @param description Self-documenting description
        @return the resulting Options instance
        :param opt:
        :param hasArg:
        :param description:
        :return:
        """
        self.addOption(opt, None, hasArg, description)
        return self

    @addOption.register(object, str, str, bool, str)
    def addOption_1(self, opt, longOpt, hasArg, description):
        """
        Add an option that contains a short-name and a long-name.
        <p>
        It may be specified as requiring an argument.
        </p>

        @param opt Short single-character name of the option.
        @param longOpt Long multi-character name of the option.
        @param hasArg flag signally if an argument is required after this option
        @param description Self-documenting description
        @return the resulting Options instance

        :param opt:
        :param longOpt:
        :param hasArg:
        :param description:
        :return:
        """
        self.addOption(Option(opt, longOpt, hasArg, description))
        return self

    @addOption.register(object, object)
    def addOption_2(self, opt):
        """
        Adds an option instance
        @param opt the option that is to be added
        @return the resulting Options instance
        :param opt:
        :return:
        """
        key = opt.getKey()

        # add it to the long option list
        if opt.hasLongOpt():
            self.longOpts.put(opt.getLongOpt(), opt)

        # if the option is required add it to the required list
        if opt.isRequired():
            if self.requiredOpts.contains(key):
                self.requiredOpts.remove(self.requiredOpts.indexOf(key))
            self.requiredOpts.add(key)

        self.shortOpts.put(key, opt)

        return self

    def addRequiredOption(self,  opt, longOpt, hasArg, description):
        """
        Add an option that contains a short-name and a long-name.
        <p>
        The added option is set as required. It may be specified as requiring an argument. This method is a shortcut for:
        </p>
        <pre>
        <code>
        Options option = new Option(opt, longOpt, hasArg, description);
        option.setRequired(true);
        options.add(option);
        </code>
        </pre>

        @param opt Short single-character name of the option.
        @param longOpt Long multi-character name of the option.
        @param hasArg flag signally if an argument is required after this option
        @param description Self-documenting description
        @return the resulting Options instance
        @since 1.4

        :param opt:
        :param longOpt:
        :param hasArg:
        :param description:
        :return:
        """
        option = Option(opt, longOpt, hasArg, description)
        option.setRequired(True)
        self.addOption(option)
        return self

    def getOptions(self):
        """
        Retrieve a read-only list of options in this set
        @return read-only Collection of {@link Option} objects in this descriptor
        """
        return Collections.unmodifiableCollection(self.helpOptions())

    def helpOptions(self):
        """
        Returns the Options for use by the HelpFormatter.
        @return the List of Options
        """
        return [self.shortOpts.values()]

    def getRequiredOptions(self):
        """
        Returns the required options.
        @return read-only List of required options
        """
        return Collections.unmodifiableList(self.requiredOpts)

    def getOption(self, opt):
        """
        Retrieve the {@link Option} matching the long or short name specified.
        <p>
        The leading hyphens in the name are ignored (up to 2).
        </p>

        @param opt short or long name of the {@link Option}
        @return the option represented by opt
        """
        opt = Util.stripLeadingHyphens(opt)
        if self.shortOpts.containsKey(opt):
            return self.shortOpts.get(opt)
        return self.longOpts.get(opt)

    def getMatchingOptions(self, opt):
        """
        Returns the options with a long name starting with the name specified.

        @param opt the partial name of the option
        @return the options matching the partial name specified, or an empty list if none matches
        @since 1.3
        """
        opt = Util.stripLeadingHyphens(opt)

        self.matchingOpts = []

        # for a perfect match return the single option only
        if self.longOpts.keySet().contains(opt):
            return Collections.singletonList(opt)

        for longOpt in self.longOpts.keySet():
            if longOpt.startsWith(opt):
                self.matchingOpts.append(longOpt)
        return self.matchingOpts

    def hasOption(self, opt):
        """
        Returns whether the named {@link Option} is a member of this {@link Options}.

        @param opt short or long name of the {@link Option}
        @return true if the named {@link Option} is a member of this {@link Options}
        """
        opt = Util.stripLeadingHyphens(opt)
        return self.shortOpts.containsKey(opt) or self.longOpts.containsKey(opt)

    def hasLongOption(self, opt):
        """
        Returns whether the named {@link Option} is a member of this {@link Options}.

        @param opt long name of the {@link Option}
        @return true if the named {@link Option} is a member of this {@link Options}
        @since 1.3
        """
        opt = Util.stripLeadingHyphens(opt)
        return self.longOpts.containsKey(opt)

    def hasShortOption(self, opt):
        """
        Returns whether the named {@link Option} is a member of this {@link Options}.

        @param opt short name of the {@link Option}
        @return true if the named {@link Option} is a member of this {@link Options}
        @since 1.3
        """

        opt = Util.stripLeadingHyphens(opt)
        return self.shortOpts.containsKey(opt)

    def getOptionGroup(self, opt):
        """
        Returns the OptionGroup the <code>opt</code> belongs to.

        @param opt the option whose OptionGroup is being queried.
        @return the OptionGroup if <code>opt</code> is part of an OptionGroup, otherwise return null
        """
        return self.optionGroups.get(opt.getKey())

    def toString(self):
        """
        Dump state, suitable for debugging.

        @return Stringified form of this object
        @Override
        """
        buf = ""
        buf += "[ Options: [ short "
        buf += f"{self.shortOpts}"
        buf += " ] [ long "
        buf += f"{self.longOpts}"
        buf += " ]"
        return buf