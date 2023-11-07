import React, { useState } from 'react';
import { View, Text, StyleSheet, TouchableOpacity } from 'react-native';

const Message = ({ text, time, isUser }) => {
    const [showTime, setShowTime] = useState(false);
    const containerStyle = isUser ? styles.userMessageContainer : styles.otherUserMessageContainer;
    const textContainerStyle = isUser ? styles.userMessageText : styles.otherUserMessageText;

    const handleTimeToggle = () => {
        if (isUser) {
            setShowTime(!showTime);
        }
    };

    return (
    <View style={[containerStyle, styles.messageContainer]}>
        <Text style={textContainerStyle}>{text}</Text>
        <TouchableOpacity
            activeOpacity={0.7}
            onPress={handleTimeToggle}
        >
            {showTime && isUser && (
                <Text style={styles.messageTime}>{time}</Text>
            )}
            <Text style={styles.messageDate}>{time.slice(0, 10)}</Text>
        </TouchableOpacity>
    </View>
    );
};

const styles = StyleSheet.create({
  messageContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    marginVertical: 5,
  },
  userMessageContainer: {
    justifyContent: 'flex-end',
  },
  otherUserMessageContainer: {
    justifyContent: 'flex-start',
  },
  userMessageText: {
    backgroundColor: '#A4C4E9',
    padding: 10,
    borderRadius: 10,
    maxWidth: '70%',
  },
  otherUserMessageText: {
    backgroundColor: '#E8E8E8',
    padding: 10,
    borderRadius: 10,
    maxWidth: '70%',
  },
  messageTime: {
    marginLeft: 5,
    color: '#AAB8C2',
  },
});

export default Message;
